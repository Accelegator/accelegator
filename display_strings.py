"""Define strings that will be displayed by the REPL."""
from map_fields import fields
from colors import bold


WELCOME = "Welcome to Accelegator, a tool that facilitates academic advising."
URL = "https://github.com/Accelegator/accelegator"

# Help display strings
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

# Help with command display strings
COMMANDS = ["help", "gensim", "list", "show", "search", "write", "quit"]
HELP_HEADER = "help\n----"
HELP_COMMAND_ONE = "help"
HELP_DESCRIPTION_ONE = "List commands and their brief descriptions"
HELP_ARGUMENTS_ONE = "None"

HELP_COMMAND_TWO = "help <command>"
HELP_DESCRIPTION_TWO = "Show verbose description of usage and show valid arguments for <command>"
HELP_ARGUMENTS_TWO = "<command>: Command to show description and valid arguments for.\nCan be any of the following\n\t" + "\n\t".join(COMMANDS)

LIST_HEADER = "list\n----"
LIST_COMMAND = "list"
LIST_DESCRIPTION = "List emails of all advisees"
LIST_ARGUMENTS = "None"

fields_list = list(fields)
fields_list.sort()
SHOW_HEADER = "show\n----"
SHOW_COMMAND_ONE = "show <email>"
SHOW_DESCRIPTION_ONE = "Display flattened (i.e. the latest response for each field) responses for advisee with <email>"
SHOW_ARGUMENTS_ONE = "<email>: Email of advisee. Include \"@allegheny.edu\""

SHOW_COMMAND_TWO = "show <email> <field>"
SHOW_DESCRIPTION_TWO = "Display all responses for advisee with <email> for given <field> (a number). Will show all previous and latest responses."
SHOW_ARGUMENTS_TWO = "<email>: Email of advisee. Include \"@allegheny.edu\"\n<field>: Can be any of the following\n\t" + "\n\t".join(fields_list)

SEARCH_HEADER = "search\n------"
SEARCH_COMMAND_ONE = "search <field>"
SEARCH_DESCRIPTION_ONE = "Search all fields of all responses of all advisees for given <keyword>"
SEARCH_ARGUMENTS_ONE = "<keyword>: Any single string"

SEARCH_COMMAND_TWO = "search <field> <keyword>"
SEARCH_DESCRIPTION_TWO = "can input any of the fields listed below and insert any keyword which would parse through the database for anything matching the keyword or anything close to it"
SEARCH_ARGUMENTS_TWO = "<keyword>: Any single string\n<field>: Can be any of the following\n\t" + "\n\t".join(fields_list)

WRITE_HEADER = "write\n-----"
WRITE_COMMAND = "write"
WRITE_DESCRIPTION = "Write the output of <command> to file (will prompt for file name)"
WRITE_ARGUMENTS = "<command>: Command whose output to write to file"

GENSIM_HEADER = "gensim\n----"
GENSIM_COMMAND_ONE = "gensim"
GENSIM_DESCRIPTION_ONE = "Perform NLP operations on every response"
GENSIM_ARGUMENTS_ONE = "None"

GENSIM_COMMAND_TWO = "gensim <target> <field>"
GENSIM_DESCRIPTION_TWO = "Perform NLP operations on <target> with <field>"
GENSIM_ARGUMENTS_TWO = "<target>: 'person' or 'question'\n<field>: specific email or question number (leave blank for all)"

QUIT_HEADER = "quit\n----"
QUIT_COMMAND = "quit"
QUIT_DESCRIPTION = "Quits the Accelegator program"
QUIT_ARGUMENTS = "None"

COMMAND_LABEL = "Command: "
DESCRIPTION_LABEL = "Description: "
ARGUMENTS_LABEL = "Arguments: "

# Command display strings
LIST_HEADER = bold("Advisees")
NO_ADVISEES = "None to list"
