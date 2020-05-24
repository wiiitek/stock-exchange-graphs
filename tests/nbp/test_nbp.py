import os
from datetime import date
from pathlib import Path
from unittest import TestCase

from src.nbp.nbp import Nbp, NonWorkingDayException


class TestCommandLineArguments(TestCase):

    def setUp(self):
        root_path = Path(__file__).parent.parent.parent
        self.sample_data_dir = os.path.join(root_path, 'tests/resources/nbp/')

    def test_should_create_instance(self):
        tested = Nbp('https://localhost')
        self.assertIsNotNone(tested)

    def test_should_throw_exception_for_saturday(self):
        tested = Nbp('https://api.nbp.pl')
        saturday = date(2020, 2, 2)
        with self.assertRaises(NonWorkingDayException):
            tested.currency_url('usd', saturday)

    def test_should_create_currency_rates_urls(self):
        tested = Nbp('https://api.nbp.pl')
        actual = tested.currency_url('usd', date(2020, 2, 3))
        expected = 'https://api.nbp.pl/api/exchangerates/rates/a/usd/2020-02-03/?format=json'
        self.assertEqual(expected, actual)

    def test_should_find_last_monday(self):
        actual = Nbp.last_monday(date(2020, 2, 9))
        expected = date(2020, 2, 3)
        self.assertEqual(expected, actual)

    def test_should_read_exchange_rate_from_json(self):
        json = '''[{
                "table":"A", "no":"095/A/NBP/2020", "effectiveDate":"2020-05-18",
                "rates":[
                    {"currency":"dolar amerykański","code":"USD","mid":4.2224},
                    {"currency":"dolar australijski","code":"AUD","mid":2.7218},
                    {"currency":"euro","code":"EUR","mid":4.5644}
                ]
        }]'''
        actual = Nbp.currency_rate('usd', json)
        expected = ('2020-05-18', 4.2224)
        self.assertEqual(expected, actual)

    def test_should_create_currency_urls(self):
        tested = Nbp('https://api.nbp.pl')
        day = date(2020, 5, 20)
        actual = tested.currency_urls(day, 'chf', 5)
        expected = [
            'https://api.nbp.pl/api/exchangerates/rates/a/chf/2020-05-18/?format=json',
            'https://api.nbp.pl/api/exchangerates/rates/a/chf/2020-05-11/?format=json',
            'https://api.nbp.pl/api/exchangerates/rates/a/chf/2020-05-04/?format=json',
            'https://api.nbp.pl/api/exchangerates/rates/a/chf/2020-04-27/?format=json',
            'https://api.nbp.pl/api/exchangerates/rates/a/chf/2020-04-20/?format=json'
        ]
        self.assertEqual(expected, actual)
