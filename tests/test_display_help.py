"""test cases for displayhelp"""

def test_help_with_unknown_command():
    command = ""
    assert display_help()

def test_help_with_list():
    print help_string
