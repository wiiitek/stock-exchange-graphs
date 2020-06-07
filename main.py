import sys

from src.arguments.arguments import CommandLineArguments


def run_project(args):
    parser = CommandLineArguments()
    parser.parse(args[1:])

    currency = parser.args.currency
    print('Hello, currency specified: %(text)s!' %
          {'text': currency})


if __name__ == '__main__':
    run_project(sys.argv)
