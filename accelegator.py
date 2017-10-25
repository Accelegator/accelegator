""" Accelegator: A Software Tool for Accelerated and Adaptive Advising """

# python libraries
import sys

# local dependencies
import display_strings
from parse_arguments import parse_arguments

if __name__ == '__main__':

    ARGUMENTS = parse_arguments(sys.argv[1:])
    print(display_strings.WELCOME)
