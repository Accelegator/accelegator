""" Takes the commands entered in the REPL and maps them to tasks """

import display_list
import display_show
import display_show_with_field
import display_search
import display_search_with_field
import queries
import logging
import write_to_file


def repl(command, key1, key2, key3, dataframe):

    if command == "list":
        print(display_list.display_list(queries.query_list(dataframe)))
        logging.debug("calling query and display for " + command)
        return 0

    if command == "show":
        if key2 == "":
            print(display_show.display_show(queries.query_show(dataframe, key1)))
            logging.debug("calling query and display for " + command + " with key " + key1)
            return 1
        else:
            print(display_show_with_field.display_show_with_field(queries.query_show_field(dataframe, key1, key2)))
            logging.debug("calling query and display for " + command + " with keys " + key1 + ", " + key2)
            return 2

    if command == "search":
        if key2 == "":
            print(display_search.display_search(queries.query_search(dataframe, key1)))
            logging.debug("calling query and display for " + command + " with key " + key1)
            return 3
        else:
            print(display_search_with_field.display_search_with_field(queries.query_search_field(dataframe, key1, key2)))
            logging.debug("calling query and display for " + command + " with keys " + key1 + ", " + key2)
            return 4

    if command == "write":

        if key1 == "list":
            logging.debug("calling write of " + key1 + " function")
            data = queries.query_list(dataframe)
            return 7

        elif key1 == "show":
            if key3 == "":
                logging.debug("calling write of " + key1 + " function with key " + key2)
                data = queries.query_show(dataframe, key2)
                return 8
            else:
                logging.debug("calling write of " + key1 + " function with keys " + key2 + ", " + key3)
                data = queries.query_show_field(dataframe, key2, key3)
                return 9

        elif key1 == "search":
            if key3 == "":
                logging.debug("calling write of " + key1 + " function with key " + key2)
                data = queries.query_search(dataframe, key2)
                return 10
            else:
                logging.debug("calling write of " + key1 + " function with keys " + key2 + ", " + key3)
                data = queries.query_search_field(dataframe, key2, key3)
                return 11

        file_name = str(input('file name: '))
        write_to_file.write(data, file_name)

    if command == "help":
        if key1 == "":
            print(display_help.display_help())
            logging.debug("calling query and display for " + command)
            return 5
        else:
            print(display_help_with_command.display_help_with_command())
            logging.debug("calling query and display for " + command)
            return 6
