""" Takes the commands entered in the REPL and maps them to tasks """

import display_list
import display_show
import display_show_with_field
import display_search
import display_search_with_field
import queries
import logging
import write_to_file

def repl(command, dataframe, key1, key2, key3):

    if command == "list":
        print(display_list(queries.query_list(dataframe)))
        logging.info("calling query and display for " + command)
        return 0

    if command == "show":
        if key2 == "":
            print(display_show(queries.query_show(dataframe, key1)))
            logging.info("calling query and display for " + command + " with key " + key1)
            return 1
        else:
            print(display_show_with_field(queries.query_show_field(dataframe, key1, key2)))
            logging.info("calling query and display for " + command + " with keys " + key1 + ", " + key2)
            return 2

    if command == "search":
        if key2 == "":
            print(display_search(queries.query_search(dataframe, key1)))
            logging.info("calling query and display for " + command + " with key " + key1)
            return 3
        else:
            print(display_search_with_field(queries.query_search_field(dataframe, key1, key2)))
            logging.info("calling query and display for " + command + " with keys " + key1 + ", " + key2)
            return 4

    if command == "write":

        if key1 == "list":
            data = queries.query_list(dataframe)

        elif key1 == "show":
            if key3 == "":
                data = queries.query_show(dataframe, key2)
            else:
                data = queries.query_show_field(dataframe, key2, key3)

        elif key1 == "search":
            if key3 == "":
                data = queries.query_search(dataframe, key2)
            else:
                data = queries.query_search_field(dataframe, key2, key3)

        file_name = str(input('file name: '))
        write_to_file.write(data, file_name)

    if command == "help":
        if key1 == "":
            print(display_help())
            logging.info("calling query and display for " + command)
            return 5
        else:
            print(display_help_with_command())
            logging.info("calling query and display for " + command)
            return 6
