from display_show import display_show


def test_display_show_with_latest_timestamp():
    """ Checks that display_show returns correct string for latest timestamp """
    result_tuple = ("email", [(("timestamp", True), "field", "response")])
    result = display_show(result_tuple)
    assert repr(result) == repr("Showing flattened responses for advisee with email \x1b[1memail\x1b[0m\n\nfield                                                          \x1b[7mtimestamp\x1b[0m\nresponse\n")


def test_display_show_with_nonlatest_timestamp():
    """ Checks that display_show returns correct string for latest timestamp """
    result_tuple = ("email", [(("timestamp", False), "field", "response")])
    result = display_show(result_tuple)
    assert repr(result) == repr("Showing flattened responses for advisee with email \x1b[1memail\x1b[0m\n\nfield                                                                  timestamp\nresponse\n")


def test_display_show_with_empty_tuple():
    """ Checks display_show's output with empty tuple"""
    result_tuple = ()
    assert display_show(result_tuple) == "No responses to display"


def test_display_show_with_none_tuple():
    """ Checks display_show's output with no tuple """

    assert display_show(None) == "No responses to display"
