"""Makes program display - displays help option, search, quit and other commands for user"""
from colors import bold
from colors import negative
from colors import underline
import logging
import textwrap
import display_strings
import map_fields


def display_help_with_command(command):
    """Return a string with verbose description and valid arguments for a command."""
    command_functions = {
        "help": display_help_help,
        "gensim": display_gensim_help,
        "list": display_list_help,
        "show": display_show_help,
        "search": display_search_help,
        "write": display_write_help,
        "quit": display_quit_help
    }

    return command_functions[command]()


def display_help_help():
    command_one_tuple = (display_strings.HELP_HEADER,
                         display_strings.HELP_COMMAND_ONE,
                         display_strings.HELP_DESCRIPTION_ONE,
                         display_strings.HELP_ARGUMENTS_ONE)
    logging.debug("Command one details: " + str(command_one_tuple))

    command_two_tuple = (display_strings.HELP_COMMAND_TWO,
                         display_strings.HELP_DESCRIPTION_TWO,
                         display_strings.HELP_ARGUMENTS_TWO)
    logging.debug("Command two details: " + str(command_two_tuple))

    return format_command_description(command_one_tuple, command_two_tuple)


def display_list_help():
    command_tuple = (display_strings.LIST_HEADER,
                     display_strings.LIST_COMMAND,
                     display_strings.LIST_DESCRIPTION,
                     display_strings.LIST_ARGUMENTS)
    logging.debug("Command details: " + str(command_tuple))

    return format_command_description(command_tuple)


def display_show_help():
    command_one_tuple = (display_strings.SHOW_HEADER,
                         display_strings.SHOW_COMMAND_ONE,
                         display_strings.SHOW_DESCRIPTION_ONE,
                         display_strings.SHOW_ARGUMENTS_ONE)
    logging.debug("Command one details: " + str(command_one_tuple))

    command_two_tuple = (display_strings.SHOW_COMMAND_TWO,
                         display_strings.SHOW_DESCRIPTION_TWO,
                         display_strings.SHOW_ARGUMENTS_TWO)
    logging.debug("Command two details: " + str(command_two_tuple))

    return format_command_description(command_one_tuple, command_two_tuple)


def display_search_help():
    command_one_tuple = (display_strings.SEARCH_HEADER,
                         display_strings.SEARCH_COMMAND_ONE,
                         display_strings.SEARCH_DESCRIPTION_ONE,
                         display_strings.SEARCH_ARGUMENTS_ONE)
    logging.debug("Command one details: " + str(command_one_tuple))

    command_two_tuple = (display_strings.SEARCH_COMMAND_TWO,
                         display_strings.SEARCH_DESCRIPTION_TWO,
                         display_strings.SEARCH_ARGUMENTS_TWO)
    logging.debug("Command two details: " + str(command_two_tuple))

    return format_command_description(command_one_tuple, command_two_tuple)


def display_write_help():
    command_tuple = (display_strings.WRITE_HEADER,
                     display_strings.WRITE_COMMAND,
                     display_strings.WRITE_DESCRIPTION,
                     display_strings.WRITE_ARGUMENTS)

    return format_command_description(command_tuple)


def display_gensim_help():
    command_one_tuple = (display_strings.GENSIM_HEADER,
                         display_strings.GENSIM_COMMAND_ONE,
                         display_strings.GENSIM_DESCRIPTION_ONE,
                         display_strings.GENSIM_ARGUMENTS_ONE)
    logging.debug("Command one details: " + str(command_one_tuple))

    command_two_tuple = (display_strings.GENSIM_COMMAND_TWO,
                         display_strings.GENSIM_DESCRIPTION_TWO,
                         display_strings.GENSIM_ARGUMENTS_TWO)
    logging.debug("Command one details: " + str(command_two_tuple))

    return format_command_description(command_one_tuple, command_two_tuple)


def display_quit_help():
    command_tuple = (display_strings.QUIT_HEADER,
                     display_strings.QUIT_COMMAND,
                     display_strings.QUIT_DESCRIPTION,
                     display_strings.QUIT_ARGUMENTS)

    return format_command_description(command_tuple)


def format_command_description(command_one_tuple, command_two_tuple=None):
    logging.info("Formatting first command")
    header = bold(command_one_tuple[0])
    command_one = command_one_tuple[1]
    description_one = command_one_tuple[2]
    arguments_one = command_one_tuple[3]
    command_one_string = header + "\n" + display_strings.COMMAND_LABEL + command_one + "\n" + \
        display_strings.DESCRIPTION_LABEL + description_one + display_strings.ARGUMENTS_LABEL + arguments_one + "\n"

    if command_two_tuple is not None:
        logging.info("Formatting second command")
        command_two = command_two_tuple[0]
        description_two = command_two_tuple[1]
        arguments_two = command_two_tuple[2]
        command_two_string = display_strings.COMMAND_LABEL + command_two + "\n" + display_strings.DESCRIPTION_LABEL + \
            description_two + "\n" + display_strings.ARGUMENTS_LABEL + arguments_two + "\n"
        return command_one_string + "\n" + command_two_string
    else:
        return command_one_string


def display_help():
    """Return a string with a list of commands and their brief descriptions."""
    logging.info("Creating help string")

    help_string = ""

    for current_index, command_tuple in enumerate(display_strings.commands_list):
        left = command_tuple[0]
        right = command_tuple[1]
        if current_index is 0:
            # accounts for ansi sequence for bolded text in header
            help_string += "{:<38s}{:<40s}".format(left, right) + "\n"
        else:
            right_list = (textwrap.wrap(right, width=40))
            for current_line, description_line in enumerate(right_list):
                if current_line is 0:
                    help_string += "{:<30s}{:<40s}".format(left, description_line) + "\n"
                else:
                    empty_space = ""
                    description_line = "\t" + description_line
                    help_string += "{:<30s}{:<40s}".format(empty_space, description_line) + "\n"

    return help_string


def display_list(list_of_advisees):
    """Return a string that is list of advisees' emails."""
    result = display_strings.LIST_HEADER + "\n"

    if not list_of_advisees or list_of_advisees is None:
        return result + display_strings.NO_ADVISEES + "\n"

    for email in list_of_advisees:
        result += str(email) + "\n"

    return result


def display_show(result_tuple):
    """ Returns string with an advisee's flattened responses. Input is in form: (email, [((timestamp, latest), field, response)]) """

    if result_tuple is None or result_tuple == ():
        logging.error("No input tuple given")
        return display_strings.NO_RESPONSES

    EMAIL_INDEX = 0
    RESPONSE_LIST_INDEX = 1

    TIMESTAMP_INDEX = 0
    TIMESTAMP_STR_INDEX = 0
    TIMESTAMP_LATEST_INDEX = 1
    FIELD_INDEX = 1
    RESPONSE_INDEX = 2

    result = textwrap.fill(display_strings.SHOW_HEADER.format(bold(result_tuple[EMAIL_INDEX])), width=80) + "\n\n"

    RESPONSE_LIST = result_tuple[RESPONSE_LIST_INDEX]

    if not RESPONSE_LIST:
        logging.error("No search results")
        return result + display_strings.NO_RESPONSES

    for response in RESPONSE_LIST:
        field = underline(map_fields.get_abbreviated_field(response[FIELD_INDEX]))
        timestamp_tuple = response[TIMESTAMP_INDEX]
        timestamp_latest = timestamp_tuple[TIMESTAMP_LATEST_INDEX]
        timestamp = negative(str(timestamp_tuple[TIMESTAMP_STR_INDEX])) if timestamp_latest else str(
            timestamp_tuple[TIMESTAMP_STR_INDEX])
        response_string = str(response[RESPONSE_INDEX])
        result += align(field, timestamp) + "\n"

        result += textwrap.fill(response_string, width=80) + "\n\n"

    return result


def display_show_with_field(result_tuple):
    """ Returns a string with an advisee's past and current responses to a given field. Input is in form: (email, field, [((timestamp, latest), response)])"""

    print("result_tuple: " + str(result_tuple))
    if result_tuple is None or result_tuple == ():
        logging.error("No input tuple given")
        print("result_tuple: " + str(result_tuple))
        return display_strings.NO_RESPONSES

    EMAIL_INDEX = 0
    FIELD_INDEX = 1
    RESPONSE_LIST_INDEX = 2

    TIMESTAMP_INDEX = 0
    TIMESTAMP_STR_INDEX = 0
    TIMESTAMP_LATEST_INDEX = 1
    RESPONSE_INDEX = 1

    result = textwrap.fill(display_strings.SHOW_WITH_FIELD_HEADER.format(bold(result_tuple[EMAIL_INDEX]), bold(map_fields.get_abbreviated_field(result_tuple[FIELD_INDEX]))), width=80) + "\n\n"

    RESPONSE_LIST = result_tuple[RESPONSE_LIST_INDEX]
    if not RESPONSE_LIST:
        logging.error("No input tuple given")
        return result + display_strings.NO_RESPONSES

    for response in RESPONSE_LIST:
        timestamp_tuple = response[TIMESTAMP_INDEX]
        timestamp_latest = timestamp_tuple[TIMESTAMP_LATEST_INDEX]
        timestamp = negative(str(timestamp_tuple[TIMESTAMP_STR_INDEX])) if timestamp_latest else str(
            timestamp_tuple[TIMESTAMP_STR_INDEX])
        response_string = str(response[RESPONSE_INDEX])
        result += timestamp + "\n" + \
            textwrap.fill(response_string, width=80) + "\n"

    return result


def display_search(result_tuple, has_field=False):
    """Return string of list of advisees with responses that match search
        query. result_tuple takes on the form:
        (keyword, [((timestamp, latest), email, field, response)])."""
    KEYWORD_INDEX = 0

    # result_tuple differs based on whether it is returned by the query_search
    # or query_search_with_field function
    RESPONSE_LIST_INDEX = 2 if has_field else 1
    FIELD_INDEX = 1 if has_field else 2
    RESPONSE_INDEX = 2 if has_field else 3

    TIMESTAMP_TUPLE_INDEX = 0
    TIMESTAMP_STRING_INDEX = 0
    TIMESTAMP_LATEST_INDEX = 1

    EMAIL_INDEX = 1
    if result_tuple is None:
        logging.error("result_tuple is None")
        return display_strings.NO_RESPONSES
    if result_tuple == ():
        logging.error("result_tuple is empty")
        return display_strings.NO_RESPONSES

    KEYWORD = bold(result_tuple[KEYWORD_INDEX])
    if has_field:
        FIELD = bold(map_fields.get_field_string(result_tuple[FIELD_INDEX]))
        result = textwrap.fill(display_strings.SEARCH_WITH_FIELD_HEADER.format(KEYWORD, bold(FIELD)), width=80) + "\n\n"
    else:
        result = textwrap.fill(display_strings.SEARCH_HEADER.format(KEYWORD), width=80) + "\n\n"

    RESPONSE_LIST = result_tuple[RESPONSE_LIST_INDEX]

    if not RESPONSE_LIST:
        logging.error("No search results")
        return result + display_strings.NO_RESPONSES

    for response_tuple in RESPONSE_LIST:
        timestamp_tuple = response_tuple[TIMESTAMP_TUPLE_INDEX]
        timestamp_latest = timestamp_tuple[TIMESTAMP_LATEST_INDEX]

        timestamp_string = str(timestamp_tuple[TIMESTAMP_STRING_INDEX])
        # if timestamp is latest, invert its color
        timestamp = negative(
            timestamp_string) if timestamp_latest else timestamp_string

        email = str(response_tuple[EMAIL_INDEX])
        response = str(response_tuple[RESPONSE_INDEX])

        if not has_field:
            field = underline(map_fields.get_abbreviated_field((response_tuple[FIELD_INDEX])))
            response_string = align(
                email,
                timestamp,
                timestamp_latest) + "\n" + field + "\n" + response + "\n\n"
        else:
            response_string = align(
                email, timestamp, timestamp_latest) + "\n" + response + "\n\n"

        result += response_string

    return result


def align(left, right, is_negative_timestamp=False):
    """ Returns string with "left" aligned to the left and "right" aligned to the right """
    if is_negative_timestamp:
        logging.debug(
            "Moving right over 8 characters to account for ansi sequence")
        # adjust right alignment of inverted timestamp to account for ansi
        # sequence
        return "{:<40s}{:>48s}".format(left, right)
    else:
        return "{:<40s}{:>40s}".format(left, right)


def display_search_with_field(result_tuple):
    """ Returns string of list of advisees with responses that match search
        query and field. result_tuple takes on the form:
        (keyword, field, [((timestamp, latest), email, response)]) """
    return display_search(result_tuple, True)
