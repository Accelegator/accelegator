""" Accelegator: A Software Tool for Accelerated and Adaptive Advising """

# python libraries
import sys
# local dependencies
from queries import parse_csv_into_dataframe
from parse_arguments import parse_arguments
import display_strings
import repl


if __name__ == '__main__':

    ARGUMENTS = parse_arguments(sys.argv[1:])
    print(display_strings.WELCOME)

    # FIXME >> should match CSV filepath written from spreadsheet.py
    CSVFILEPATH = "testing.nocommit.csv"
    DATAFRAME = parse_csv_into_dataframe(CSVFILEPATH)

    command = str(input('>>> '))
    key1 = ""
    key2 = ""
    key3 = ""
    defined_commands = {"list", "show", "search", "write", "help", "quit"}
    fSet = frozenset(defined_commands)
    while command != "quit":
        keywords = command.rsplit()
        command = keywords[0]
        while keywords[0] not in defined_commands:
            print("invalid command")
            command = str(input('>>> '))
            keywords = command.rsplit()
        if len(keywords) == 2:
            key1 = keywords[1]
        elif len(keywords) == 3:
            key1 = keywords[1]
            key2 = keywords[2]
        elif len(keywords) == 4:
            key1 = keywords[1]
            key2 = keywords[2]
            key3 = keywords[3]
        repl.repl(command, command, key1, key2, key3)
        command = str(input('>>> '))
