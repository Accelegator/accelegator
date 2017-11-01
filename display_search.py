""" Returns string of list of advisees with responses
    that match search query. """
# Implementation will be moved to display.py once completed

# external dependencies
import logging
from colors import negative
from colors import bold

def display_search(result_tuple, has_field=False):
    """ Returns string of list of advisees with responses that match search
        query. result_tuple takes on the form:
        (keyword, [((timestamp, latest), email, field, response)]) """
    KEYWORD_INDEX = 0

    # result_tuple differs based on whether it is returned by the query_search or query_search_with_field function
    RESPONSE_LIST_INDEX = 2 if has_field else 1
    FIELD_INDEX = 1 if has_field else 2
    RESPONSE_INDEX = 2 if has_field else 3

    TIMESTAMP_TUPLE_INDEX = 0
    TIMESTAMP_STRING_INDEX = 0
    TIMESTAMP_LATEST_INDEX = 1

    EMAIL_INDEX = 1

    if result_tuple is None:
        logging.error("result_tuple parameter is None")
        return "No results to display"
    if result_tuple is ():
        logging.error("result_tuple is empty")
        return "No results to display"

    KEYWORD = bold(result_tuple[KEYWORD_INDEX])
    if has_field:
        FIELD = bold(result_tuple[FIELD_INDEX])
        result = "Displaying search results for keyword " + \
            KEYWORD + " in field " + FIELD + "\n\n"
    else:
        result = "Displaying search results for keyword " + KEYWORD + "\n\n"

    for response_tuple in result_tuple[RESPONSE_LIST_INDEX]:
        timestamp_tuple = response_tuple[TIMESTAMP_TUPLE_INDEX]
        timestamp_latest = timestamp_tuple[TIMESTAMP_LATEST_INDEX]

        timestamp_string = str(timestamp_tuple[TIMESTAMP_STRING_INDEX])
        # if timestamp is latest, invert its color
        timestamp = negative(
            timestamp_string) if timestamp_latest else timestamp_string

        email = str(response_tuple[EMAIL_INDEX])
        response = str(response_tuple[RESPONSE_INDEX])

        if not has_field:
            field = str(response_tuple[FIELD_INDEX])
            response_string = align(
                email,
                timestamp,
                timestamp_latest) + "\n" + field + "\n" + response + "\n\n"
        else:
            response_string = align(
                email, timestamp, timestamp_latest) + "\n" + response + "\n\n"

        result += response_string

    return result


def align(left, right, is_negative_timestamp=False):
    """ Returns string with "left" aligned to the left and "right" aligned to the right """
    if is_negative_timestamp:
        logging.debug(
            "Moving right over 8 characters to account for ansi sequence")
        # adjust right alignment of inverted timestamp to account for ansi
        # sequence
        return "{:<40s}{:>48s}".format(left, right)
    else:
        return "{:<40s}{:>40s}".format(left, right)
