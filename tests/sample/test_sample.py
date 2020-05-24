from unittest import TestCase

from src.sample.sample import concat


class TestSample(TestCase):

    def test_concat(self):
        self.assertEqual('123', concat([1, 2, 3]), 'Should be 123')

    def test_nested_concat(self):
        self.assertEqual('122', concat((1, 2, 2)), 'Should be 122')
