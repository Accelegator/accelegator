import display


def test_display_show_with_latest_timestamp():
    """Check that display_show returns correct string for latest timestamp."""
    result_tuple = ("email", [(("timestamp", True), "1. What name would you like to be called by?", "response")])
    result = display.display_show(result_tuple)
    assert repr(result) == repr("Showing flattened responses for advisee with email \x1b[1memail\x1b[0m\n\n\x1b[4mname\x1b[0m                                                   \x1b[7mtimestamp\x1b[0m\nresponse\n\n")


def test_display_show_with_nonlatest_timestamp():
    """ Check that display_show returns correct string for latest timestamp."""
    result_tuple = ("email", [(("timestamp", False), "1. What name would you like to be called by?", "response")])
    result = display.display_show(result_tuple)
    assert repr(result) == repr("Showing flattened responses for advisee with email \x1b[1memail\x1b[0m\n\n\x1b[4mname\x1b[0m                                                           timestamp\nresponse\n\n")


def test_display_show_with_empty_tuple():
    """Check display_show's output with empty tuple."""
    result_tuple = ()
    assert display.display_show(result_tuple) == "No responses to list"


def test_display_show_with_none_tuple():
    """Check display_show's output with no tuple."""

    assert display.display_show(None) == "No responses to list"
