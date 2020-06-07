from datetime import date
from unittest import TestCase

from src.nbp.nbp_url import NbpUrl


class TestNbpUrl(TestCase):

    def test_should_return_simple_url(self):
        tested = NbpUrl()

        actual = tested.currency_urls(date(2020, 5, 1), date(2020, 6, 1))

        self.assertEqual([
            'https://api.nbp.pl/api/exchangerates/tables/a/2020-05-01/2020-06-01/?format=json'
        ], actual)

    def test_should_return_urls_for_regular_ranges(self):
        tested = NbpUrl(nbp_range=2)
        expected = [
            'https://api.nbp.pl/api/exchangerates/tables/a/2020-05-01/2020-05-02/?format=json',
            'https://api.nbp.pl/api/exchangerates/tables/a/2020-05-03/2020-05-04/?format=json'
        ]

        actual = tested.currency_urls(date(2020, 5, 1), date(2020, 5, 4))

        self.assertEqual(expected, actual)

    def test_should_return_urls_for_last_range_partial(self):
        tested = NbpUrl(nbp_range=3)
        expected = [
            'https://api.nbp.pl/api/exchangerates/tables/a/2020-05-01/2020-05-03/?format=json',
            'https://api.nbp.pl/api/exchangerates/tables/a/2020-05-04/2020-05-04/?format=json'
        ]

        actual = tested.currency_urls(date(2020, 5, 1), date(2020, 5, 4))

        self.assertEqual(expected, actual)
