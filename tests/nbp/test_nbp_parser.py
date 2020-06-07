import os
from pathlib import Path
from unittest import TestCase

from src.nbp.nbp_parser import NbpParser


class TestNbpParser(TestCase):

    def setUp(self):
        root_path = Path(__file__).parent.parent.parent
        self.sample_data_dir = os.path.join(root_path, 'tests', 'resources', 'nbp')
        small_file = os.path.join(self.sample_data_dir, 'parser', 'small-table-a.json')
        big_file = os.path.join(self.sample_data_dir, 'parser', 'big-table-a.json')
        with open(small_file, mode='r') as file:
            content = file.read()
            self.tested_small = NbpParser(content)
            file.close()
        with open(big_file, mode='r') as file:
            content = file.read()
            self.tested_big = NbpParser(content)
            file.close()

    def test_should_read_eur(self):
        actual = self.tested_small.currency_rates('EUR', '2020-06-04')

        self.assertEqual({'2020-06-04': 4.4347}, actual)

    def test_should_read_eur_two(self):
        actual = self.tested_small.currency_rates('EUR', '2020-06-04', '2020-06-05')

        self.assertEqual({
            '2020-06-04': 4.4347,
            '2020-06-05': 4.4443}, actual)

    def test_should_read_eur_multiple_from_big_file(self):
        actual = self.tested_big.currency_rates('EUR',
                                                '2020-05-05',
                                                '2020-05-12',
                                                '2020-05-19',
                                                '2020-06-05')
        self.assertEqual({
            '2020-05-05': 4.5476,
            '2020-05-12': 4.5549,
            '2020-05-19': 4.5610,
            '2020-06-05': 4.4443}, actual)

    def test_should_read_two_swiss_franks(self):
        actual = self.tested_small.currency_rates('CHF', '2020-06-04', '2020-06-05')

        self.assertEqual({'2020-06-04': 4.1190, '2020-06-05': 4.0948}, actual)

    def test_should_read_two_swiss_franks_from_big_file(self):
        actual = self.tested_big.currency_rates('CHF', '2020-06-04', '2020-06-05')

        self.assertEqual({'2020-06-04': 4.1190, '2020-06-05': 4.0948}, actual)
