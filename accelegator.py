""" Accelegator: A Software Tool for Accelerated and Adaptive Advising """

# python libraries
import sys
# local dependencies
from queries import parse_csv_into_dataframe
from parse_arguments import parse_arguments
import display_strings
from defaults import DEFAULT_CSVFILE
from spreadsheet import create_csv
import repl
import route_commands
import write_to_file
import logging


if __name__ == '__main__':

    ARGUMENTS = parse_arguments(sys.argv[1:])
    print(display_strings.WELCOME)
    create_csv()

    DATAFRAME = parse_csv_into_dataframe(DEFAULT_CSVFILE)

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
            print("Invalid command. Type \"help\" to see list of valid commands.")
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
        call = route_commands.route_commands(command, arg1, arg2)
        output = repl.repl(DATAFRAME, call, command, arg1, arg2, arg3)
        if (call == 6):
            inner_call = route_commands.route_commands(arg1, arg2, arg3)
            output = repl.repl(DATAFRAME, inner_call, command, arg1, arg2, arg3)
            file_name = str(input('File to write to: '))
            logging.info("Writing to file: " + file_name)
            write_to_file.write(output, file_name)
        else:
            print(output)

        arg1 = ""
        arg2 = ""
        arg3 = ""
        command = str(input('>>> '))
