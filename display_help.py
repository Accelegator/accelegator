""" Displays a list of commands and their brief descriptions """
from colors import bold
# Implementation will be moved to display.py once completed

def display_help():

    tup1 = (bold("Command") , bold("Descriptions"))
    tup2 = ("quit" ,"exit the program")
    tup3 = ("show<email>","display flattened responses for advisee with <email>")
    tup4 = ("help <command>", "list descriptions for said command and show available commands for program")
    tup5 = ("help","list commands and brief descriptions")
    tup6 = ("show <email> <field>","display responses for given field, incl. history")
    tup7 = ("list", "list advisees by emails & show latest response date")
    tup8 = ("search <keyword>" , "search all fields of all responses of all students fpr keyword " )
    tup9 = ("search <field> <keyword>","search given of all responses of all students for keyword")
    tup10 = ("write command", "write command to output to file (prompt for filepath)")


    commands_list = []

    commands_list.append(tup1)
    commands_list.append(tup2)
    commands_list.append(tup3)
    commands_list.append(tup4)
    commands_list.append(tup5)
    commands_list.append(tup6)
    commands_list.append(tup7)
    commands_list.append(tup8)
    commands_list.append(tup9)
    commands_list.append(tup10)

    help_string = ""

    for current_index, command_tuple in enumerate(commands_list):
        if current_index == 0:
            help_string += "{:<40s}{:<56s}".format(command_tuple[0], command_tuple[1])+"\n"
        else :
            help_string += "{:<40s}{:<48s}".format(command_tuple[0], command_tuple[1])+"\n"
    return help_string
