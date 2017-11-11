""" Takes the call numbers and routes them to commands """

import logging
import display
import queries
from map_fields import get_field_int


def repl(dataframe, call, command, arg1, arg2):

    if call == 1:
        return display.display_list(queries.query_list(dataframe))
        logging.debug("calling query and display for " + command)

    elif call == 2:
        return display.display_show(queries.query_show(dataframe, arg1))
        logging.debug(
            "calling query and display for " +
            command +
            " with arg " +
            arg1)

    elif call == 3:
        return display.display_show_with_field(
            queries.query_show_field(
                dataframe, arg1, get_field_int(arg2)))
        logging.debug(
            "calling query and display for " +
            command +
            " with args " +
            arg1 +
            ", " +
            arg2)

    elif call == 4:
        return (display.display_search(queries.query_search(dataframe, arg1)))
        logging.debug(
            "calling query and display for " +
            command +
            " with arg " +
            arg1)

    elif call == 5:
        return display.display_search_with_field(
            queries.query_search_field(
                dataframe, get_field_int(arg1), arg2))
        logging.debug(
            "calling query and display for " +
            command +
            " with args " +
            arg1 +
            ", " +
            arg2)

    elif call == 7:
        return display.display_help()
        logging.debug("calling query and display for " + command)

    elif call == 8:
        return display.display_help_with_command(arg1)
        logging.debug("calling query and display for " + command)
