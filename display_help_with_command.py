""" Display verbose description and valid arguments for a command """

# Implementation will be moved to display.py once completed

def display_help_with_command(command):
    command_strings {
        "show" : display_help_show
        "quit" : display_help_quit
        "show <email>" : display_help_show
        "help <command>": display_help
        "help": display_help
        "show <email> <field>": display_help_show
        "list": display_list
        "search <keyword>" : display_search_keyword
        "search <field> <keyword>" : display_search_keyword
        "write command" : display_write_command
    }
    return command_string[command]()

def display_write_command(display_help_with_command):
    header = "write command\n--------"
    command = "write command"
    description = "write command output to file(prompt for filepath)"
    arguments = "none"

    return header + format_command_description(command, description, arguments)

def display_list(display_help_with_command):
    header = "list\n -----"
    command = "list"
    description = " list advisees by emails & shows latest response date"
    arguments = "none"

    return header + format_command_description(command, description, arguments)

def display_search_keyword(display_help_with_command):
    header = "search <keyword>"
    command_one = "search <keyword>"
    command_two = "seach <field> <keyword>"
    description = "can input any of the fields listed below and insert any keyword which would parse through the database for anything matching the keyword or anything close to it"
    arguments = {"fields can be any of the following"
    "allegheny-email"
    "id"
    "name"
    "resume"
    "cover-letter"
    "four-year-plan"
    "grad-year"
    "github"
    "website"
    "linkedin"
    "twitter"
    "fav-major-class"
    "fav-nonmajor-class"
    "career"command_one = "help"
    "academic-interests"
    "personal-interests"
    "tech-strengths"
    "tech-weaknesses"
    "academic-status"
    "personal-status"
    "advisor-questions"}

return header + format_command_description_show(command_one, command_two, description, arguments)

def display_help_quit(display_help_with_command): list advisees by emails & shows latest response date
    header = "quit\n----"
    command = "quit"
    description = "Quits the Accelegator program"
    arguments = "None"

    return header + format_command_description(command, description, arguments)

def display_help_show(display_help_with_command):
    header = "show\n----"
    command_one = "show <email>"
    command_two = "show <email> <field>"
    description = "Description"

    arguments = {"Advisee's email written without the '@alleghenycommand_one = "help".edu' ending. Ex. 'kimy'
"fields can be any of the following"
"allegheny-email"
"id"
"name"
"resume"
"cover-letter"
"four-year-plan"
"grad-year"
"github"
"website"
"linkedin"
"twitter"
"fav-major-class"
"fav-nonmajor-class"
"career"command_one = "help"
"academic-interests"
"personal-interests"
"tech-strengths"
"tech-weaknesses"
"academic-status"
"personal-status"
"advisor-questions"}

    return header + format_command_description_show(command_one, command_two, description, arguments)



def format_command_description(command, description, arguments):
    return command + "\n" + "Description: " + description + "\nArguments: " + arguments + "\n"

def format_command_description_show(command_one, command_two, description, arguments):
    return "Commands: " + "\n" + command_one + "\n" + command_two + "\n" + "Description: " + description + "\nArguments: "+ arguments
