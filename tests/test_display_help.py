import display


def test_display_help():
    """ Check if correct string with correct formatting is returned """
    expected_help_string = """\x1b[1mCommand\x1b[0m                       \x1b[1mDescription\x1b[0m                     \nhelp                          List commands and their brief           \n                              \tdescriptions                           \nhelp <command>                List verbose description of <command>   \n                              \tand show valid arguments for <command> \nlist                          List emails of all advisees             \nshow <email>                  Display flattened responses for advisee \n                              \twith <email>                           \nshow <email> <field>          Display all responses for advisee with  \n                              \t<email> given <field>                  \nsearch <keyword>              Search all fields of all responses of   \n                              \tall advisees for <keyword>             \nsearch <field> <keyword>      Search given <field> of all responses of\n                              \tall advisees for <keyword>             \nwrite <command>               Write <command> output to file (will    \n                              \tprompt for file name)                  \nquit                          Exit the program                        \n"""
    actual_help_string = display.display_help()

    assert repr(actual_help_string) == repr(expected_help_string)
