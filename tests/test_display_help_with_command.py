import display


def test_display_help_with_command_help():
    """ Checks if correct string is returned for help command """
    expected_help_string = """\x1b[1mhelp\n----\x1b[0m\nCommand: help\nDescription: List commands and their brief descriptions\nArguments: None\n\nCommand: help <command>\nDescription: Show verbose description of usage and show valid arguments for <command>\nArguments: <command>: Command to show description and valid arguments for. Can be any of the following\n\thelp\n\tlist\n\tshow\n\tsearch\n\twrite\n\tquit\n"""
    actual_help_string = display.display_help_with_command("help")

    assert repr(actual_help_string) == repr(expected_help_string)


def test_display_help_with_command_show():
    """ Checks if correct string is returned for show command """
    expected_help_string = """\x1b[1mshow\n----\x1b[0m\nCommand: show <email>\nDescription: Display flattened (i.e. the latest response for each field) responses for advisee with <email>\nArguments: <email>: Email of advisee. Include "@allegheny.edu"\n\nCommand: show <email> <field>\nDescription: Display all responses for advisee with <email> for given <field> (a number). Will show all previous and latest responses.\nArguments: <email>: Email of advisee. Include "@allegheny.edu"\n<field>: Can be any of the following\n\t1:allegheny-email\n\t2:name\n\t3:id\n\t4:grad-year\n\t5:major\n\t6:second-major\n\t7:minor\n\t8:second-minor\n\t9:resume\n\t10:academic-status\n\t11:personal-status\n\t12:cover-letter\n\t13:twitter\n\t14:linkedin\n\t15:website\n\t16:fav-major-class\n\t17:fav-nonmajor-class\n\t18:career\n\t19:academic-interests\n\t20:personal-interests\n\t21:tech-strengths\n\t22:tech-weaknesses\n\t23:hows-school\n\t24:advisor-questions\n"""
    actual_help_string = display.display_help_with_command("show")

    assert repr(actual_help_string) == repr(expected_help_string)


def test_display_help_with_command_list():
    """ Checks if correct string is returned for list command """
    expected_help_string = """\x1b[1mlist\n----\x1b[0m\nCommand: list\nDescription: List emails of all advisees\nArguments: None\n"""
    actual_help_string = display.display_help_with_command("list")

    assert repr(actual_help_string) == repr(expected_help_string)


def test_display_help_with_command_search():
    """ Checks if correct string is returned for search command """
    expected_help_string = """\x1b[1msearch\n------\x1b[0m\nCommand: search <field>\nDescription: Search all fields of all responses of all advisees for given <keyword>\nArguments: <keyword>: Any single string\n\nCommand: search <field> <keyword>\nDescription: can input any of the fields listed below and insert any keyword which would parse through the database for anything matching the keyword or anything close to it\nArguments: <keyword>: Any single string\n<field>: Can be any of the following\n\t1:allegheny-email\n\t2:name\n\t3:id\n\t4:grad-year\n\t5:major\n\t6:second-major\n\t7:minor\n\t8:second-minor\n\t9:resume\n\t10:academic-status\n\t11:personal-status\n\t12:cover-letter\n\t13:twitter\n\t14:linkedin\n\t15:website\n\t16:fav-major-class\n\t17:fav-nonmajor-class\n\t18:career\n\t19:academic-interests\n\t20:personal-interests\n\t21:tech-strengths\n\t22:tech-weaknesses\n\t23:hows-school\n\t24:advisor-questions\n"""
    actual_help_string = display.display_help_with_command("search")

    assert repr(actual_help_string) == repr(expected_help_string)


def test_display_help_with_command_write():
    """ Checks if correct string is returned for write command """
    expected_help_string = """\x1b[1mwrite\n-----\x1b[0m\nCommand: write\nDescription: Write the output of <command> to file (will prompt for file name)\nArguments: <command>: Command whose output to write to file\n"""
    actual_help_string = display.display_help_with_command("write")

    assert repr(actual_help_string) == repr(expected_help_string)


def test_display_help_with_command_quit():
    """ Checks if correct string is returned for quit command """
    expected_help_string = """\x1b[1mquit\n----\x1b[0m\nCommand: quit\nDescription: Quits the Accelegator program\nArguments: None\n"""
    actual_help_string = display.display_help_with_command("quit")

    assert repr(actual_help_string) == repr(expected_help_string)
