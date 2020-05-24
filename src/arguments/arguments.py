from argparse import ArgumentParser, Namespace


class CommandLineArguments(object):

    def __init__(self):
        self.parser = ArgumentParser()
        self.parser.add_argument('-n',
                                 '--name',
                                 required=True,
                                 dest='name',
                                 help='Sample parameter')
        # namespace will be overwritten by parse method
        self.known: Namespace = Namespace()

    def parse(self, args=None):
        self.known = self.parser.parse_args(args)
