import os
from datetime import date
from pathlib import Path
from unittest import TestCase

from src.nbp.nbp import Nbp
from src.nbp.nbp_http import NbpHttp

NBP_API_DOMAIN = 'https://api.nbp.pl'


class TestNbp(TestCase):

    def setUp(self):
        root_path = Path(__file__).parent.parent.parent
        self.sample_data_dir = os.path.join(root_path, 'tests', 'resources', 'nbp')

    def test_should_create_instance(self):
        tested = Nbp('https://localhost', NbpHttp())
        self.assertIsNotNone(tested)

    def test_should_create_currency_rates_urls(self):
        tested = Nbp(NBP_API_DOMAIN, NbpHttp())
        actual = tested.currency_urls(date(2020, 2, 3), date(2020, 2, 14))
        expected = [
            'https://api.nbp.pl/api/exchangerates/tables/a/2020-02-03/2020-02-14/?format=json'
        ]
        self.assertEqual(expected, actual)

    def test_should_create_currency_urls(self):
        tested = Nbp(NBP_API_DOMAIN, NbpHttp())
        actual = tested.currency_urls(date(2020, 1, 1), date(2020, 6, 6))
        expected = [
            'https://api.nbp.pl/api/exchangerates/tables/a/2020-01-01/2020-03-30/?format=json',
            'https://api.nbp.pl/api/exchangerates/tables/a/2020-03-31/2020-06-06/?format=json'
        ]
        self.assertEqual(expected, actual)
