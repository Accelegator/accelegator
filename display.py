from colors import bold
from colors import negative
import logging
import textwrap


def display_help_with_command(command):
    """ Returns a string with verbose description and valid arguments for a command """
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
    header = "help\n----"
    command_one = "help"
    description_one = "List commands and their brief descriptions"
    arguments_one = "None"
    command_one_tuple = (header, command_one, description_one, arguments_one)
    logging.debug("Command one details: " + str(command_one_tuple))

    command_two = "help <command>"
    description_two = "Show verbose description of usage and show valid arguments for <command>"
    arguments_two = "<command>: Command to show description and valid arguments for. Can be any of the following\n\thelp\n\tgensim\n\tlist\n\tshow\n\tsearch\n\twrite\n\tquit"
    command_two_tuple = (command_two, description_two, arguments_two)
    logging.debug("Command two details: " + str(command_two_tuple))

    return format_command_description(command_one_tuple, command_two_tuple)


def display_list_help():
    header = "list\n----"
    command = "list"
    description = "List emails of all advisees"
    arguments = "None"
    command_tuple = (header, command, description, arguments)
    logging.debug("Command details: " + str(command_tuple))

    return format_command_description(command_tuple)


def display_show_help():
    header = "show\n----"
    command_one = "show <email>"
    description_one = "Display flattened (i.e. the latest response for each field) responses for advisee with <email>"
    arguments_one = "<email>: Email of advisee. Include \"@allegheny.edu\""
    command_one_tuple = (header, command_one, description_one, arguments_one)
    logging.debug("Command one details: " + str(command_one_tuple))

    command_two = "show <email> <field>"
    description_two = "Display all responses for advisee with <email> for given <field>. Will show all previous and latest responses."
    arguments_two = "<email>: Email of advisee. Include \"@allegheny.edu\"\n<field>: Can be any of the following\n\tallegheny-email\n\tid\n\tname\n\tresume\n\tcover-letter\n\tfour-year-plan\n\tgrad-year\n\tgithub\n\twebsite\n\tlinkedin\n\ttwitter\n\tfav-major-class\n\tfav-nonmajor-class\n\tcareer\n\tacademic-interests\n\tpersonal-interests\n\ttech-strengths\n\ttech-weaknesses\n\tacademic-status\n\tpersonal-status\n\tadvisor-questions"
    command_two_tuple = (command_two, description_two, arguments_two)
    logging.debug("Command two details: " + str(command_two_tuple))

    return format_command_description(command_one_tuple, command_two_tuple)


def display_search_help():
    header = "search\n----"
    command_one = "search <field>"
    description_one = "Search all fields of all responses of all advisees for given <keyword>"
    arguments_one = "<keyword>: Any single string"
    command_one_tuple = (header, command_one, description_one, arguments_one)
    logging.debug("Command one details: " + str(command_one_tuple))

    command_two = "search <field> <keyword>"
    description_two = "can input any of the fields listed below and insert any keyword which would parse through the database for anything matching the keyword or anything close to it"
    arguments_two = "<keyword>: Any single string\n<field>: Can be any of the following\n\tallegheny-email\n\tid\n\tname\n\tresume\n\tcover-letter\n\tfour-year-plan\n\tgrad-year\n\tgithub\n\twebsite\n\tlinkedin\n\ttwitter\n\tfav-major-class\n\tfav-nonmajor-class\n\tcareer\n\tacademic-interests\n\tpersonal-interests\n\ttech-strengths\n\ttech-weaknesses\n\tacademic-status\n\tpersonal-status\n\tadvisor-questions"
    command_two_tuple = (command_two, description_two, arguments_two)
    logging.debug("Command two details: " + str(command_two_tuple))

    return format_command_description(command_one_tuple, command_two_tuple)


def display_write_help():
    header = "write\n----"
    command = "write"
    description = "Write the output of <command> to file (will prompt for file name)"
    arguments = "<command>: Command whose output to write to file"
    command_tuple = (header, command, description, arguments)

    return format_command_description(command_tuple)
    
def display_gensim_help():
    header = "gensim\n----"
    command_one = "gensim <target> <field>"
    description_one = "Perform NLP operations on <target> with <field>"
    arguments_one = "<target>: 'person' or 'question'\n<field>: specific email or question number (leave blank for all)"
    command_one_tuple = (header, command_one, description_one, arguments_one)
    logging.debug("Command one details: " + str(command_one_tuple))
    
    return format_command_description(command_one_tuple)


def display_quit_help():
    header = "quit\n----"
    command = "quit"
    description = "Quits the Accelegator program"
    arguments = "None"

    command_tuple = (header, command, description, arguments)

    return format_command_description(command_tuple)


def format_command_description(command_one_tuple, command_two_tuple=None):
    logging.info("Formatting first command")
    header = bold(command_one_tuple[0])
    command_one = command_one_tuple[1]
    description_one = command_one_tuple[2]
    arguments_one = command_one_tuple[3]
    command_one_string = header + "\n" + "Command: " + command_one + "\n" + "Description: " + description_one + "\nArguments: " + arguments_one + "\n"

    if command_two_tuple is not None:
        logging.info("Formatting second command")
        command_two = command_two_tuple[0]
        description_two = command_two_tuple[1]
        arguments_two = command_two_tuple[2]
        command_two_string = "Command: " + command_two + "\n" + "Description: " + description_two + "\nArguments: " + arguments_two + "\n"
        return command_one_string + "\n" + command_two_string
    else:
        return command_one_string


def display_help():
    """ Returns a string with a list of commands and their brief descriptions """
    logging.info("Creating help string")

    commands_list = []

    commands_list.append((bold("Command"), bold("Description")))
    commands_list.append(("help", "List commands and their brief descriptions"))
    commands_list.append(("help <command>", "List verbose description of <command> and show valid arguments for <command>"))
    commands_list.append(("gensim <target> <field>", "Perform NLP based on <target> with specifier <field>"))
    commands_list.append(("list", "List emails of all advisees"))
    commands_list.append(("show <email>", "Display flattened responses for advisee with <email>"))
    commands_list.append(("show <email> <field>", "Display all responses for advisee with <email> given <field>"))
    commands_list.append(("search <keyword>", "Search all fields of all responses of all advisees for <keyword>"))
    commands_list.append(("search <field> <keyword>", "Search given <field> of all responses of all advisees for <keyword>"))
    commands_list.append(("write <command>", "Write <command> output to file (will prompt for file name)"))
    commands_list.append(("quit", "Exit the program"))

    help_string = ""

    for current_index, command_tuple in enumerate(commands_list):
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
    """ Returns a string that is list of advisees' emails """
    result = bold("Advisees") + "\n"

    if not list_of_advisees or list_of_advisees is None:
        return result + "None to list\n"

    for email in list_of_advisees:
        result += str(email) + "\n"

    return result


def display_search(result_tuple, has_field=False):
    """ Returns string of list of advisees with responses that match search
        query. result_tuple takes on the form:
        (keyword, [((timestamp, latest), email, field, response)]) """
    KEYWORD_INDEX = 0

    # result_tuple differs based on whether it is returned by the query_search or query_search_with_field function
    RESPONSE_LIST_INDEX = 2 if has_field else 1
    FIELD_INDEX = 1 if has_field else 2
    RESPONSE_INDEX = 2 if has_field else 3

    TIMESTAMP_TUPLE_INDEX = 0
    TIMESTAMP_STRING_INDEX = 0
    TIMESTAMP_LATEST_INDEX = 1

    EMAIL_INDEX = 1

    if result_tuple is None:
        logging.error("result_tuple parameter is None")
        return "No input tuple given"
    if result_tuple is ():
        logging.error("result_tuple is empty")
        return "No input tuple given"

    KEYWORD = bold(result_tuple[KEYWORD_INDEX])
    if has_field:
        FIELD = bold(result_tuple[FIELD_INDEX])
        result = "Displaying search results for keyword " + \
            KEYWORD + " in field " + FIELD + "\n\n"
    else:
        result = "Displaying search results for keyword " + KEYWORD + "\n\n"

    response_list = result_tuple[RESPONSE_LIST_INDEX]

    if not response_list:
        logging.error("No search results")
        return result + "No responses to display"

    for response_tuple in response_list:
        timestamp_tuple = response_tuple[TIMESTAMP_TUPLE_INDEX]
        timestamp_latest = timestamp_tuple[TIMESTAMP_LATEST_INDEX]

        timestamp_string = str(timestamp_tuple[TIMESTAMP_STRING_INDEX])
        # if timestamp is latest, invert its color
        timestamp = negative(
            timestamp_string) if timestamp_latest else timestamp_string

        email = str(response_tuple[EMAIL_INDEX])
        response = str(response_tuple[RESPONSE_INDEX])

        if not has_field:
            field = str(response_tuple[FIELD_INDEX])
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


def display_show(result_tuple):
    """ Returns string with an advisee's flattened responses. Input is in form: (email, [((timestamp, latest), field, response)]) """

    if result_tuple is None or result_tuple is ():
        logging.error("No input tuple given")
        return "No tuple exists"

    EMAIL_INDEX = 0
    RESPONSE_LIST_INDEX = 1

    TIMESTAMP_INDEX = 0
    TIMESTAMP_STR_INDEX = 0
    TIMESTAMP_LATEST_INDEX = 1
    FIELD_INDEX = 1
    RESPONSE_INDEX = 2

    result = textwrap.fill("Showing flattened responses for advisee with email " + bold(str(result_tuple[EMAIL_INDEX])), 80) + "\n\n"

    response_list = result_tuple[RESPONSE_LIST_INDEX]

    if not response_list:
        logging.error("No search results")
        return result + "No responses to display"

    for response in response_list:
        field = str(response[FIELD_INDEX])
        timestamp_tuple = response[TIMESTAMP_INDEX]
        timestamp_latest = timestamp_tuple[TIMESTAMP_LATEST_INDEX]
        timestamp = negative(str(timestamp_tuple[TIMESTAMP_STR_INDEX])) if timestamp_latest else str(timestamp_tuple[TIMESTAMP_STR_INDEX])
        response_string = str(response[RESPONSE_INDEX])
        result += align(field, timestamp) + "\n"

        result += textwrap.fill(response_string, width=80) + "\n\n"

    return result


def display_show_with_field(result_tuple):
    """ Returns a string with an advisee's past and current responses to a given field. Input is in form: (email, field, [((timestamp, latest), response)])"""

    if result_tuple is None or result_tuple is ():
        logging.error("No input tuple given")
        return "No responses to display"

    EMAIL_INDEX = 0
    FIELD_INDEX = 1
    RESPONSE_LIST_INDEX = 2

    TIMESTAMP_INDEX = 0
    TIMESTAMP_STR_INDEX = 0
    TIMESTAMP_LATEST_INDEX = 1
    RESPONSE_INDEX = 1

    result = textwrap.fill("Showing responses for advisee with email " + bold(str(result_tuple[EMAIL_INDEX])) + " to field " + bold(str(result_tuple[FIELD_INDEX])), 80) + "\n\n"

    for response in result_tuple[RESPONSE_LIST_INDEX]:
        timestamp_tuple = response[TIMESTAMP_INDEX]
        timestamp_latest = timestamp_tuple[TIMESTAMP_LATEST_INDEX]
        timestamp = negative(str(timestamp_tuple[TIMESTAMP_STR_INDEX])) if timestamp_latest else str(timestamp_tuple[TIMESTAMP_STR_INDEX])
        response_string = str(response[RESPONSE_INDEX])
        result += timestamp + "\n" + textwrap.fill(response_string, width=80) + "\n"

    return result
