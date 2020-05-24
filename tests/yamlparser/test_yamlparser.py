import os
from pathlib import Path
from unittest import TestCase

from src.yamlparser.yamlparser import YamlParser


class TestCommandLineArguments(TestCase):

    def setUp(self):
        root_path = Path(__file__).parent.parent.parent
        self.simple_yaml_path = os.path.join(root_path, 'tests/resources/sample.yml')

    def test_should_read_simple_yaml_value(self):
        tested = YamlParser(self.simple_yaml_path)
        actual = tested.get('key1')
        self.assertEqual('abcdefgh', actual, 'should read value')

    def test_should_read_simple_yaml_array(self):
        tested = YamlParser(self.simple_yaml_path)
        actual = tested.get('key2')
        self.assertEqual([1, 2, 3], actual, 'should read array')

    def test_should_read_simple_yaml_map(self):
        tested = YamlParser(self.simple_yaml_path)
        actual = tested.get('key3')
        self.assertEqual({'key3a': 3.1, 'key3b': '12345'}, actual, 'should read map')
