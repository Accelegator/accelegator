# internal dependencies
import display


def test_display_search_with_field_with_valid_result_tuple():
    """ Checks if display_search_with_field() returns correct string when result_tuple is valid """
    result_tuple = ("keyword", 2, [(("timestamp", True), "email", "response")])
    result = display.display_search_with_field(result_tuple)
    num_of_spaces = 66
    assert repr(result) == repr("Displaying search results for keyword \x1b[1mkeyword\x1b[0m in field \x1b[1mname\x1b[0m\n\n" + "email" + ' ' * num_of_spaces + "\x1b[7mtimestamp\x1b[0m\nresponse\n\n")


def test_display_search_with_field_with_empty_tuple():
    """ Checks if display_search() returns correct string when result_tuple is empty """
    result_tuple = ()
    result = display.display_search_with_field(result_tuple)

    assert result == "No responses to list"


def test_display_search_with_field_with_none_tuple():
    """ Checks if display_search_with_field() returns correct string when result_tuple is None """
    result = display.display_search_with_field(None)

    assert result == "No responses to list"


def test_display_search_with_field_with_integer_timestamp():
    """ Checks if display_search() returns correct heading string when result_tuple is valid """
    result_tuple = ("keyword", 2, [((31102017, True), "email", "response")])
    result = display.display_search_with_field(result_tuple)
    num_of_spaces = 67
    assert repr(result) == repr("Displaying search results for keyword \x1b[1mkeyword\x1b[0m in field \x1b[1mname\x1b[0m\n\n" + "email" + ' ' * num_of_spaces + "\x1b[7m31102017\x1b[0m\nresponse\n\n")
