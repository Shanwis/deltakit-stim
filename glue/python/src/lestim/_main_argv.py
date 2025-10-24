import sys

import lestim


def main_argv():
    lestim.main(command_line_args=sys.argv[1:])


if __name__ == '__main__':
    main_argv()
