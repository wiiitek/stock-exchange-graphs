from argparse import ArgumentParser, Namespace


class CommandLineArguments(object):

    def __init__(self):
        self.parser = ArgumentParser()
        self.parser.add_argument('-c',
                                 '--currency',
                                 required=True,
                                 dest='currency',
                                 help='Currency symbol for data import (GBP, USD, EUR, CHF).')
        # namespace will be overwritten by parse method
        self.args: Namespace = Namespace()

    def parse(self, args=None):
        self.args = self.parser.parse_args(args)
