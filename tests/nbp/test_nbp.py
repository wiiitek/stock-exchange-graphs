import csv
import os
from datetime import date
from pathlib import Path
from unittest import TestCase

from src.nbp.nbp import Nbp, NonWorkingDayException

NBP_API_DOMAIN = 'https://api.nbp.pl'


class TestCommandLineArguments(TestCase):

    def setUp(self):
        root_path = Path(__file__).parent.parent.parent
        self.sample_data_dir = os.path.join(root_path, 'tests', 'resources', 'nbp')

    def test_should_create_instance(self):
        tested = Nbp('https://localhost')
        self.assertIsNotNone(tested)

    def test_should_throw_exception_for_saturday(self):
        tested = Nbp(NBP_API_DOMAIN)
        saturday = date(2020, 2, 2)
        with self.assertRaises(NonWorkingDayException):
            tested.currency_url('usd', saturday)

    def test_should_create_currency_rates_urls(self):
        tested = Nbp(NBP_API_DOMAIN)
        actual = tested.currency_url('usd', date(2020, 2, 3))
        expected = 'https://api.nbp.pl/api/exchangerates/rates/a/usd/2020-02-03/?format=json'
        self.assertEqual(expected, actual)

    def test_should_find_last_monday(self):
        actual = Nbp.last_monday(date(2020, 2, 9))
        expected = date(2020, 2, 3)
        self.assertEqual(expected, actual)

    def test_should_read_exchange_rate_from_json(self):
        json = '''{
                "table":"A","currency":"frank szwajcarski","code":"CHF",
                "rates":[
                    {"no":"095/A/NBP/2020","effectiveDate":"2020-05-18","mid":4.3419}
                ]
        }'''
        actual = Nbp.currency_rate(json)
        expected = ('2020-05-18', 4.3419)
        self.assertEqual(expected, actual)

    def test_should_create_currency_urls(self):
        tested = Nbp(NBP_API_DOMAIN)
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

    def test_should_parse_json_multiple(self):
        json_a = '''{
                        "table":"A","currency":"dolar amerykański","code":"USD",
                        "rates":[
                            {"no":"095/A/NBP/2020","effectiveDate":"2020-05-18","mid":4.2224}
        ]}'''
        json_b = '''{
                        "table":"A","currency":"dolar amerykański","code":"USD",
                        "rates":[
                            {"no":"090/A/NBP/2020","effectiveDate":"2020-05-11","mid":4.2126}
        ]}'''
        actual = Nbp.currency_rates([json_a, json_b])
        expected = [('2020-05-11', 4.2126), ('2020-05-18', 4.2224)]
        self.assertEqual(expected, actual)

    def test_should_save_to_csv_file(self):
        data = [('2020-05-11', 0.9997), ('2020-05-18', 0.9998), ('2020-05-25', 0.9999)]

        tmp_file = os.path.join(self.sample_data_dir, 'test.csv')
        if os.path.isfile(tmp_file):
            os.remove(tmp_file)

        Nbp.save_to_csv(tmp_file, data)

        line_count = 0
        with open(tmp_file) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            for _ in csv_reader:
                line_count += 1
            csv_file.close()

        self.assertEqual(3, line_count)
