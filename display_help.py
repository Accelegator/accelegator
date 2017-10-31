""" Displays a list of commands and their brief descriptions """

# Implementation will be moved to display.py once completed

def display_help(help):

    return  "{:<40s}{:<48s}".format('Commands, descriptions');
            "{:<40s}{:<48s}".format('quit, exit the program');
            "{:<40s}{:<48s}".format('show <email>, display flattened responses for advisee with <email>');
            "{:<40s}{:<48s}".format('help <command>, verbose descriptions of commands & args');
            "{:<40s}{:<48s}".format('help, list commands & brief descriptions');
            "{:<40s}{:<48s}".format('show <email> <field>, display responses for given field, incl. history');
            "{:<40s}{:<48s}".format('list, list advisees by emails & shows latest response date');
            "{:<40s}{:<48s}".format('search <keyword>, search all fields of all responses of all students for keyword');
            "{:<40s}{:<48s}".format('search <field> <keyword>, search given of all responses of all students for keyword');
            "{:<40s}{:<48s}".format('write command, write command output to file(prompt for filepath)');
