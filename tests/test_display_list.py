# internal dependencies
import display


def test_display_list_with_none_list():
    """ Checks if correct string is returned when no list is passed in """
    list_string = display.display_list(None)

    assert list_string == "\x1b[1mAdvisees\x1b[0m\nNo advisees to list\n"


def test_display_list_with_empty_list():
    """ Checks if correct string is returned when empty list is passed in """
    list_string = display.display_list([])

    assert list_string == "\x1b[1mAdvisees\x1b[0m\nNo advisees to list\n"


def test_display_list_with_string_list():
    """ Checks if correct string is returned when string list is passed in """
    list_to_display = ["email1", "email2", "email3"]
    list_string = display.display_list(list_to_display)

    assert list_string == "\x1b[1mAdvisees\x1b[0m\nemail1\nemail2\nemail3\n"


def test_display_list_with_int_list():
    """ Checks if correct string is returned when int list is passed in """
    list_to_display = [1, 2, 3]
    list_string = display.display_list(list_to_display)

    assert list_string == "\x1b[1mAdvisees\x1b[0m\n1\n2\n3\n"
