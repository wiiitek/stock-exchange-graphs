from unittest import TestCase

from src.arguments.arguments import CommandLineArguments


class TestCommandLineArguments(TestCase):

    def setUp(self):
        self.tested = CommandLineArguments()

    def test_should_exit_with_code_2_for_missing_input_invoice(self):
        self.assertRaisesRegex(SystemExit, '^2$', self.tested.parse)

    def test_should_parse_short_name_param(self):
        self.tested.parse(['-n', 'źdźbło'])
        actual = self.tested.known.name
        self.assertEqual(actual, 'źdźbło')

    def test_should_parse_long_name_param(self):
        self.tested.parse(['--name', '   '])
        actual = self.tested.known.name
        self.assertEqual(actual, '   ')
