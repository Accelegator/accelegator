""" Display verbose description and valid arguments for a command """

# Implementation will be moved to display.py once completed
from colors import bold
import logging


def display_help_with_command(command):
    command_functions = {
        "help": display_help_help,
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
    arguments_two = "<command>: Command to show description and valid arguments for. Can be any of the following\n\thelp\n\tlist\n\tshow\n\tsearch\n\twrite\n\tquit"
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
    command_one = "show <emai>"
    description_one = "Display flattened (i.e. the latest response for each field) responses for advisee with <email>"
    arguments_one = "<email>: Email of advisee. Do not include \"@allegheny.edu\""
    command_one_tuple = (header, command_one, description_one, arguments_one)
    logging.debug("Command one details: " + str(command_one_tuple))

    command_two = "show <email> <field>"
    description_two = "Display all responses for advisee with <email> for given <field>. Will show all previous and latest responses."
    arguments_two = "<email>: Email of advisee. Do not include \"@allegheny.edu\"\n<field>: Can be any of the following\n\tallegheny-email\n\tid\n\tname\n\tresume\n\tcover-letter\n\tfour-year-plan\n\tgrad-year\n\tgithub\n\twebsite\n\tlinkedin\n\ttwitter\n\tfav-major-class\n\tfav-nonmajor-class\n\tcareer\n\tacademic-interests\n\tpersonal-interests\n\ttech-strengths\n\ttech-weaknesses\n\tacademic-status\n\tpersonal-status\n\tadvisor-questions"
    command_two_tuple = (command_two, description_two, arguments_two)
    logging.debug("Command two details: " + str(command_two_tuple))

    return format_command_description(command_one_tuple, command_two_tuple)


def display_search_help():
    header = "search\n------"
    command_one = "search <field>"
    description_one = "Search all fields of all responses of all advisees for given <keyword>"
    arguments_one = "<keyword>: Any single string"
    command_one_tuple = (header, command_one, description_one, arguments_one)
    logging.debug("Command one details: " + str(command_one_tuple))

    command_two = "seach <field> <keyword>"
    description_two = "can input any of the fields listed below and insert any keyword which would parse through the database for anything matching the keyword or anything close to it"
    arguments_two = "<keyword>: Any single string\n<field>: Can be any of the following\n\tallegheny-email\n\tid\n\tname\n\tresume\n\tcover-letter\n\tfour-year-plan\n\tgrad-year\n\tgithub\n\twebsite\n\tlinkedin\n\ttwitter\n\tfav-major-class\n\tfav-nonmajor-class\n\tcareer\n\tacademic-interests\n\tpersonal-interests\n\ttech-strengths\n\ttech-weaknesses\n\tacademic-status\n\tpersonal-status\n\tadvisor-questions"
    command_two_tuple = (command_two, description_two, arguments_two)
    logging.debug("Command two details: " + str(command_two_tuple))

    return format_command_description(command_one_tuple, command_two_tuple)


def display_write_help():
    header = "write\n-----"
    command = "write"
    description = "Write the output of <command> to file (will prompt for file name)"
    arguments = "<command>: Command whose output to write to file"
    command_tuple = (header, command, description, arguments)

    return format_command_description(command_tuple)


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
