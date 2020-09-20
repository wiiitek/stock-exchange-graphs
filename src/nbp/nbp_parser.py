import json
from datetime import date, timedelta

NBP_DATE_FORMAT = '%Y-%m-%d'


class StartAfterEndException(Exception):
    pass


def initialize(start: date, end: date):
    result = {}
    day_count = (end - start).days
    if day_count < 0:
        raise StartAfterEndException('start: ' + start.strftime(NBP_DATE_FORMAT) + ', end: ' + end.strftime(NBP_DATE_FORMAT))
    for n in range(day_count + 1):
        single_date = start + timedelta(n)
        result[single_date.strftime(NBP_DATE_FORMAT)] = None
    return result


class NbpParser(object):
    """For parsing currency rates JSON from NBP api: https://api.nbp.pl/en.html#kursyWalut."""

    def __init__(self, nbp_api_json: str):
        self.json = nbp_api_json

    def currency_rates(self, currency_id: str, start: date, end: date = None):
        """Parses JSON for multiple currencies and multiples dates
           and extract currency rates into map: date -> rate."""
        if end is None:
            end = start
        result = initialize(start, end)

        parsed = json.loads(self.json)
        for table in parsed:
            effective_date = table['effectiveDate']
            if effective_date in result:
                for rate in table['rates']:
                    if rate['code'] == currency_id:
                        result[effective_date] = rate['mid']
        return result
