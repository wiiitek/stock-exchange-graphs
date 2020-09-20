from datetime import date

from src.nbp.nbp_http import _call_for_currency
from src.nbp.nbp_parser import NbpParser
from src.nbp.nbp_url import NbpUrl


class NonWorkingDayException(Exception):
    pass


class Nbp(object):
    """Facade for interaction with NBP api for currency rates."""
    # for now we are only reading from table A
    # https://www.nbp.pl/home.aspx?f=/kursy/kursy_archiwum.html
    table_name: str = 'a'

    call_for_currency = _call_for_currency

    def __init__(self, api_domain):
        self.api_domain = api_domain
        self.nbp_url = NbpUrl()

    def currency_urls(self, start: date, end: date):
        return self.nbp_url.currency_urls(start, end)

    def currency_rates(self, currency_id: str, start: date, end: date):
        urls = self.currency_urls(start, end)

        for idx, url in urls:
            response = self.call_for_currency(url)
            parser = NbpParser(response)
            parser.currency_rates(currency_id, start, end)
