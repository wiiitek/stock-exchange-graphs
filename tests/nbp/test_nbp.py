import csv
import os
from datetime import date
from pathlib import Path
from unittest import TestCase

from src.nbp.nbp import Nbp

NBP_API_DOMAIN = 'https://api.nbp.pl'


class TestNbp(TestCase):

    def setUp(self):
        root_path = Path(__file__).parent.parent.parent
        self.sample_data_dir = os.path.join(root_path, 'tests', 'resources', 'nbp')

    def test_should_create_instance(self):
        tested = Nbp('https://localhost')
        self.assertIsNotNone(tested)

    def test_should_create_currency_rates_urls(self):
        tested = Nbp(NBP_API_DOMAIN)
        actual = tested.currency_urls(date(2020, 2, 3), date(2020, 2, 14))
        expected = [
            'https://api.nbp.pl/api/exchangerates/tables/a/2020-02-03/2020-02-14/?format=json'
        ]
        self.assertEqual(expected, actual)

    def test_should_create_currency_urls(self):
        tested = Nbp(NBP_API_DOMAIN)
        actual = tested.currency_urls(date(2020, 1, 1), date(2020, 6, 6))
        expected = [
            'https://api.nbp.pl/api/exchangerates/tables/a/2020-01-01/2020-03-30/?format=json',
            'https://api.nbp.pl/api/exchangerates/tables/a/2020-03-31/2020-06-06/?format=json'
        ]
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
