""" Displays a list of commands and their brief descriptions """

# Implementation will be moved to display.py once completed

def display_help(help):
    Help = """Commands
            show <email>                      display flattened responses for advisee with <email>
            help <command>                    display verbose descriptions of <command> and valid arguments
            help                              list commands & brief descriptions
            quit                              exit the program
            show <email> <field>              display responses for given field, incl. history
            list                              list advisees by emails, show latest response date
            search <keyword>                  search all fields of all responses of all students for keyword
            Search <field> <keyword>          search given of all responses of all students for keyword
            write command                     write command output to file (prompt for filepath)""";

    return Help; 
