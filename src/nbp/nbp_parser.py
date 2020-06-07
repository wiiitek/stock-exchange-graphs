import json


class NbpParser(object):
    """For parsing currency rates JSON from NBP api: https://api.nbp.pl/en.html#kursyWalut."""

    def __init__(self, nbp_api_json: str):
        self.json = nbp_api_json

    def currency_rates(self, currency_id: str, *dates: str):
        """Parses JSON for multiple currencies and multiples dates
           and extract currency rates into map: date -> rate."""
        result = {}
        parsed = json.loads(self.json)
        for table in parsed:
            effective_date = table['effectiveDate']
            if effective_date in dates:
                for rate in table['rates']:
                    if rate['code'] == currency_id:
                        result[effective_date] = rate['mid']
        return result
