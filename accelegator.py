# python libraries
import sys
import logging

# local dependencies
import display_strings
import display_help_with_command
import display_help
from parse_arguments import parse_arguments

if __name__ == '__main__':

    arguments = parse_arguments(sys.argv[1:])
    print(display_strings.WELCOME)
    print(display_help_with_command.display_help_with_command("quit"))
