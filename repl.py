""" Takes the call numbers and routes them to commands """

import display_list
import display_show
import display_show_with_field
import display_search
import display_search_with_field
import queries
import logging
import write_to_file


def repl(command, arg1, arg2, arg3, dataframe, call):

    if call == 1:
        print(display_list.display_list(queries.query_list(dataframe)))
        logging.debug("calling query and display for " + command)

    elif call == 2:
        print(display_show.display_show(queries.query_show(dataframe, arg1)))
        logging.debug("calling query and display for " + command + " with arg " + arg1)

    elif call == 3:
        print(display_show_with_field.display_show_with_field(queries.query_show_field(dataframe, arg1, arg2)))
        logging.debug("calling query and display for " + command + " with args " + arg1 + ", " + arg2)

    elif call == 4:
        print(display_search.display_search(queries.query_search(dataframe, arg1)))
        logging.debug("calling query and display for " + command + " with arg " + arg1)

    elif call == 5:
        print(display_search_with_field.display_search_with_field(queries.query_search_field(dataframe, arg1, arg2)))
        logging.debug("calling query and display for " + command + " with args " + arg1 + ", " + arg2)

    elif call == 6:
        logging.debug("calling write of " + arg1 + " function")
        data = queries.query_list(dataframe)
        file_name = str(input('file name: '))
        write_to_file.write(data, file_name)

    elif call == 7:
        logging.debug("calling write of " + arg1 + " function with arg " + arg2)
        data = queries.query_show(dataframe, arg2)
        file_name = str(input('file name: '))
        write_to_file.write(data, file_name)

    elif call == 8:
        logging.debug("calling write of " + arg1 + " function with args " + arg2 + ", " + arg3)
        data = queries.query_show_field(dataframe, arg2, arg3)
        file_name = str(input('file name: '))
        write_to_file.write(data, file_name)

    elif call == 9:
        logging.debug("calling write of " + arg1 + " function with arg " + arg2)
        data = queries.query_search(dataframe, arg2)
        file_name = str(input('file name: '))
        write_to_file.write(data, file_name)

    elif call == 10:
        logging.debug("calling write of " + arg1 + " function with args " + arg2 + ", " + arg3)
        data = queries.query_search_field(dataframe, arg2, arg3)
        file_name = str(input('file name: '))
        write_to_file.write(data, file_name)

    elif call == 11:
        print(display_help.display_help())
        logging.debug("calling query and display for " + command)

    elif call == 12:
        print(display_help_with_command.display_help_with_command())
        logging.debug("calling query and display for " + command)
