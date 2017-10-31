""" Display verbose description and valid arguments for a command """

# Implementation will be moved to display.py once completed

def display_help_with_command(command):
    command_strings {
        "show" : display_help_show
        "quit" : display_help_quit
        "show <email>" : display_show_email
        "help <command>": display_help_with_command
        "help": display_help
        "show <email> <field>": display_show_email_field
        "list": display_list
        "search <keyword>" : display_search_keyword
        "search <field> <keyword>" : display_search_field_keyword
        "write command" : display_write_command
    }
    command_string[command]()

def display_help_quit():
    header = "quit\n----"
    command = "quit"
    description = "Quits the Accelegator program"
    arguments = "None"
    
    return header + format_command_description(command, description, arguments)

def display_help_show():
    header = "show\n----"
    command_one = "show <email>"
    command_two = "show <email> <field>"
    description = "Description"

    arguments = {"Advisee's email written without the '@allegheny.edu' ending. Ex. 'kimy'
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
"career"
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
