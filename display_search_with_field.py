""" Returns string of list of advisees with responses
    that match search query and field. """
# Implementation will be moved to display.py once completed

from display_search import display_search


def display_search_with_field(result_tuple):
    """ Returns string of list of advisees with responses that match search
        query and field. result_tuple takes on the form:
        (keyword, field, [((timestamp, latest), email, response)]) """
    return display_search(result_tuple, True)
