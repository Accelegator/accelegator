# internal dependencies
import display_list


def test_display_list_with_none_list():

    list_string = display_list.display_list(None)

    assert list_string == "\x1b[1mAdvisees\x1b[0m\nNone to list\n"


def test_display_list_with_empty_list():

    list_string = display_list.display_list([])

    assert list_string == "\x1b[1mAdvisees\x1b[0m\nNone to list\n"


def test_display_list_with_string_list():

    list_to_display = ["email1", "email2", "email3"]
    list_string = display_list.display_list(list_to_display)

    assert list_string == "\x1b[1mAdvisees\x1b[0m\nemail1\nemail2\nemail3\n"


def test_display_list_with_int_list():

    list_to_display = [1, 2, 3]
    list_string = display_list.display_list(list_to_display)

    assert list_string == "\x1b[1mAdvisees\x1b[0m\n1\n2\n3\n"
