import sys

from src.arguments.arguments import CommandLineArguments


def run_project(args):
    arguments = CommandLineArguments()
    arguments.parse(args[1:])

    name = arguments.known.invoice_input
    print('Hello %(name)s!' %
          {'name': name})


if __name__ == '__main__':
    run_project(sys.argv)
