""" Displays a list of commands and their brief descriptions """

# Implementation will be moved to display.py once completed

def display_help(help):

    return  "{:<40s}{:<48s}".format("Commands" , "descriptions")+"\n"+
            "{:<40s}{:<48s}".format("quit", "exit the program")+"\n"+
            "{:<40s}{:<48s}".format("show <email>" , " display flattened responses for advisee with <email>")+"\n"+
            "{:<40s}{:<48s}".format("help <command>", "descriptions")+"\n"+
            "{:<40s}{:<48s}".format("help", "list commands & brief descriptions")+"\n"+
            "{:<40s}{:<48s}".format("show <email> <field>", "display responses for given field, incl. history")+"\n"+
            "{:<40s}{:<48s}".format("list", "list advisees by emails & shows latest response date")+"\n"+
            "{:<40s}{:<48s}".format("search <keyword>", "search all fields of all responses of all students for keyword")+"\n"+
            "{:<40s}{:<48s}".format("search <field> <keyword>", "search given of all responses of all students for keyword")+"\n"+
            "{:<40s}{:<48s}".format("write command"," write command output to file(prompt for filepath)")+"\n"
