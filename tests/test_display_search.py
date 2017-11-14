# internal dependencies
import display


def test_display_search_with_latest_timestamp():
    """Check display_search() returns correct string if timestamp is latest (should be in negative color)."""
    result_tuple = ("keyword", [(("timestamp", True), "email", "1. What name would you like to be called by?", "response")])
    result = display.display_search(result_tuple)
    num_of_spaces = 66
    assert repr(result) == repr("Displaying search results for keyword \x1b[1mkeyword\x1b[0m\n\n" + "email" + ' ' * num_of_spaces + "\x1b[7mtimestamp\x1b[0m\n\x1b[4mname\x1b[0m\nresponse\n\n")


def test_display_search_with_non_latest_timestamp():
    """Check display_search() returns correct string if timestamp is not latest."""
    result_tuple = ("keyword", [(("timestamp", False), "email", "1. What name would you like to be called by?", "response")])
    result = display.display_search(result_tuple)
    num_of_spaces = 66
    assert repr(result) == repr("Displaying search results for keyword \x1b[1mkeyword\x1b[0m\n\n" + "email" + ' ' * num_of_spaces + "timestamp\n\x1b[4mname\x1b[0m\nresponse\n\n")


def test_display_search_with_field_with_empty_tuple():
    """Check if display_search() returns correct string when result_tuple is empty."""
    result_tuple = ()
    result = display.display_search(result_tuple)

    assert result == "No responses to list"


def test_display_search_with_field_with_none_tuple():
    """Check if display_search_with_field() returns correct string when result_tuple is None."""
    result = display.display_search(None)

    assert result == "No responses to list"


def test_align_with_negative_timestamp():
    """Check that align() returns properly aligned string, accounting for the ansi escape sequences in the negative colored timestamp."""
    aligned = display.align("email", "\x1b[7mtimestamp\x1b[0m", True)
    assert len(aligned) == 88


def test_align_without_negative_timestamp():
    """Check that align() returns properly aligned string."""
    aligned = display.align("email", "timestamp")
    assert len(aligned) == 80
