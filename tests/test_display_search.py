# internal dependencies
import display


def test_display_search_with_latest_timestamp():
    """ Checks display_search() returns correct string if timestamp is latest (should be in negative color) """
    result_tuple = ("keyword", [(("timestamp", True), "email", "field", "response")])
    result = display.display_search(result_tuple)
    num_of_spaces = 66
    assert repr(result) == repr("Displaying search results for keyword \x1b[1mkeyword\x1b[0m\n\n" + "email" + ' ' * num_of_spaces + "\x1b[7mtimestamp\x1b[0m\nfield\nresponse\n\n")


def test_display_search_with_non_latest_timestamp():
    """ Checks display_search() returns correct string if timestamp is not latest """
    result_tuple = ("keyword", [(("timestamp", False), "email", "field", "response")])
    result = display.display_search(result_tuple)
    num_of_spaces = 66
    assert repr(result) == repr("Displaying search results for keyword \x1b[1mkeyword\x1b[0m\n\n" + "email" + ' ' * num_of_spaces + "timestamp\nfield\nresponse\n\n")


def test_display_search_with_field_with_empty_tuple():
    """ Checks if display_search() returns correct string when result_tuple is empty """
    result_tuple = ()
    result = display.display_search(result_tuple)

    assert result == "No input tuple given"


def test_display_search_with_field_with_none_tuple():
    """ Checks if display_search_with_field() returns correct string when result_tuple is None """
    result = display.display_search(None)

    assert result == "No input tuple given"


def test_align_with_negative_timestamp():
    """ Checks that align() returns properly aligned string, accounting for the ansi escape sequences in the negative colored timestamp """
    aligned = display.align("email", "\x1b[7mtimestamp\x1b[0m", True)
    assert len(aligned) == 88


def test_align_without_negative_timestamp():
    """ Checks that align() returns properly aligned string """
    aligned = display.align("email", "timestamp")
    assert len(aligned) == 80
