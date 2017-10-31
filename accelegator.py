""" Accelegator: A Software Tool for Accelerated and Adaptive Advising """

# python libraries
import sys

# local dependencies
#from parser import parse_csv_into_dataframe
from parse_arguments import parse_arguments
import display_strings
import repl

if __name__ == '__main__':

    ARGUMENTS = parse_arguments(sys.argv[1:])
    print(display_strings.WELCOME)

    # FIXME >> should match CSV filepath written from spreadsheet.py
    CSVFILEPATH = "testing.nocommit.csv"
    #DATAFRAME = parse_csv_into_dataframe(CSVFILEPATH)

    command = str(input('>>> '))
    defined_commands = {"list", "show", "search", "quit"}
    fSet = frozenset(defined_commands)
    while command not in defined_commands:
        print("invalid command")
        command = str(input('>>> '))
    while command != "quit":
        repl.repl(command)
        command = str(input('>>> '))
