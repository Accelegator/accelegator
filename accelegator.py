""" Accelegator: A Software Tool for Accelerated and Adaptive Advising """

# python libraries
import sys

# local dependencies
from parser import parse_csv_into_dataframe
from parse_arguments import parse_arguments
import display_strings
import repl
import route_commands

if __name__ == '__main__':

    ARGUMENTS = parse_arguments(sys.argv[1:])
    print(display_strings.WELCOME)

    # FIXME >> should match CSV filepath written from spreadsheet.py
    CSVFILEPATH = "testing.nocommit.csv"
    DATAFRAME = parse_csv_into_dataframe(CSVFILEPATH)

    command = str(input('>>> '))
    arg1 = ""
    arg2 = ""
    arg3 = ""
    call = 0
    defined_commands = {"list", "show", "search", "write", "help", "quit"}
    fSet = frozenset(defined_commands)
    args = []
    while command != "quit":
        args = command.rsplit()
        command = args[0]
        while args[0] not in defined_commands:
            print("invalid command")
            command = str(input('>>> '))
            args = command.rsplit()
            command = args[0]
        if len(args) == 2:
            arg1 = args[1]
        elif len(args) == 3:
            arg1 = args[1]
            arg2 = args[2]
        elif len(args) == 4:
            arg1 = args[1]
            arg2 = args[2]
            arg3 = args[3]
        call = route_commands.route_commands(command, arg1, arg2, arg3)
        repl.repl(command, arg1, arg2, arg3, DATAFRAME, call)
        command = str(input('>>> '))
