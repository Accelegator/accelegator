""" Displays a list of commands and their brief descriptions """

# Implementation will be moved to display.py once completed

def display_help(help):
    print("Commands");
    print("show <email>                   display flattened responses for advisee with <email>");
    print("help <command>              display verbose descriptions of <command> and valid arguments");
    print("help                        list commands & brief descriptions  ");
    print("quit                         exit the program");
    print("show <email> <field>         display responses for given field, incl. history");
    print("list                         list advisees by emails, show latest response date");\
    print("search <keyword>             search all fields of all responses of all students for keyword");
    print("Search <field> <keyword>     ");
    print("write command                write command output to file (prompt for filepath)");
    
return;
