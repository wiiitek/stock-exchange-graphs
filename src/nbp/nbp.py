from datetime import timedelta

from src.nbp.nbp_days import _last_monday
from src.nbp.nbp_http import _call_for_currency
from src.nbp.nbp_parser import _currency_rate
from src.nbp.nbp_parser import _currency_rates


class NonWorkingDayException(Exception):
    pass


class Nbp(object):
    # https://www.nbp.pl/home.aspx?f=/kursy/kursy_archiwum.html
    table_name: str = 'a'

    last_monday = _last_monday
    call_for_currency = _call_for_currency
    currency_rate = _currency_rate
    currency_rates = _currency_rates

    def __init__(self, api_domain):
        self.api_domain = api_domain

    def currency_url(self, currency_id, day):
        weekday = day.weekday()
        if weekday in [6, 7]:
            raise NonWorkingDayException(f'Day: {day} is non-working-day')
        day_str = day.strftime("%Y-%m-%d")
        return f'{self.api_domain}/api/exchangerates/rates/{Nbp.table_name}/{currency_id}/{day_str}/?format=json'

    def currency_urls(self, day, currency_id, weeks):
        result = []
        current_day = Nbp.last_monday(day)
        for x in range(0, weeks):
            url = self.currency_url(currency_id, current_day)
            result.append(url)
            current_day = current_day - timedelta(weeks=1)
        return result