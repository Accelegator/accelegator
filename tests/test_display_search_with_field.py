# internal dependencies
from display_search_with_field import display_search_with_field


def test_display_search_with_field():
    list = [(("timestamp", True), "keyword", "email", "field", "response")]
    result = display_search_with_field(list)
    num_of_spaces = 66
    assert repr(result) == repr("Displaying search results for keyword \x1b[1mkeyword\x1b[0m in field \x1b[1mfield\x1b[0m\n\n" + "email" + ' ' * num_of_spaces + "\x1b[7mtimestamp\x1b[0m\nfield\nresponse\n\n")
