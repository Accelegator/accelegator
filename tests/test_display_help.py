import display_help


def test_display_help():
    expected_help_string = """\x1b[1mCommand\x1b[0m                       \x1b[1mDescriptions\x1b[0m                    \nhelp                          list commands and brief descriptions    \nhelp <command>                list verbose description of <command>   \n                              \tand show available arguments for       \n                              \t<command>                              \nlist                          list emails of all advisees             \nshow <email>                  display flattened responses for advisee \n                              \twith <email>                           \nshow <email> <field>          display all responses for advisee with  \n                              \t<email> given <field>                  \nsearch <keyword>              search all fields of all responses of   \n                              \tall students for <keyword>             \nsearch <field> <keyword>      search given <field> of all responses of\n                              \tall students for <keyword>             \nwrite <command>               write <command> output to file (will    \n                              \tprompt for file name)                  \nquit                          exit the program                        \n"""
    actual_help_string = display_help.display_help()
    assert repr(actual_help_string) == repr(expected_help_string)
