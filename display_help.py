""" Displays a list of commands and their brief descriptions """
from colors import bold
import textwrap
import logging
# Implementation will be moved to display.py once completed


def display_help():

    logging.info("Creating help string")

    commands_list = []

    commands_list.append((bold("Command"), bold("Description")))
    commands_list.append(("help", "List commands and their brief descriptions"))
    commands_list.append(("help <command>", "List verbose description of <command> and show available arguments for <command>"))
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
