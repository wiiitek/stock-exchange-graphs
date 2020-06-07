from datetime import date, timedelta

NBP_API_DOMAIN = 'https://api.nbp.pl'
"""Domain for NBP api calls."""

NBP_DAYS_RANGE = 90
"""A single enquiry cannot cover a period longer than 93 days."""

DATE_FORMAT = '%Y-%m-%d'


def _min(date_a: date, date_b: date):
    if date_a > date_b:
        return date_b
    return date_a


class NbpUrl(object):
    """For creating URLs to retrieve currency rates from NBP api"""

    def __init__(self, domain: str = NBP_API_DOMAIN, nbp_range: int = NBP_DAYS_RANGE):
        self.domain = domain
        self.nbp_range = nbp_range

    def currency_urls(self, start: date, end: date):
        result = []

        start_date = start

        while start_date <= end:
            end_date = start_date + timedelta(days=self.nbp_range - 1)
            smaller_end = _min(end, end_date)
            url = self._url(start_date, smaller_end)
            result.append(url)
            # prepare for next iteration
            start_date = start_date + timedelta(days=self.nbp_range)

        return result

    def _url(self, start: date, end: date):
        start_str = start.strftime(DATE_FORMAT)
        end_str = end.strftime(DATE_FORMAT)
        return f'{self.domain}/api/exchangerates/tables/a/{start_str}/{end_str}/?format=json'
