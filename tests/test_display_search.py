# internal dependencies
from display_search import display_search
from display_search import align


def test_display_search_with_latest_timestamp():
    list = [(("timestamp", True), "keyword", "email", "field", "response")]
    result = display_search(list)
    num_of_spaces = 66
    assert repr(result) == repr("Displaying search results for keyword \x1b[1mkeyword\x1b[0m\n\n" + "email" + ' ' * num_of_spaces + "\x1b[7mtimestamp\x1b[0m\nfield\nresponse\n\n")


def test_display_search_with_non_latest_timestamp():
    list = [(("timestamp", False), "keyword", "email", "field", "response")]
    result = display_search(list)
    num_of_spaces = 66
    assert repr(result) == repr("Displaying search results for keyword \x1b[1mkeyword\x1b[0m\n\n" + "email" + ' ' * num_of_spaces + "timestamp\nfield\nresponse\n\n")


def test_align_with_negative_timestamp():
    aligned = align("email", "\x1b[7mtimestamp\x1b[0m", True)
    assert len(aligned) == 88


def test_align_without_negative_timestamp():
    aligned = align("email", "timestamp")
    assert len(aligned) == 80
