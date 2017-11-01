""" Returns a string with an advisee's past and current responses to a given field. """
import textwrap
import logging
from colors import bold
from colors import negative


def display_show_with_field(result_tuple):
    """ Returns a string with an advisee's past and current responses to a given field. Input is in form: (email, field, [((timestamp, latest), response)])"""

    if not result_tuple:
        logging.error("No input tuple given")
        return "No responses to display"

    EMAIL_INDEX = 0
    FIELD_INDEX = 1
    RESPONSE_LIST_INDEX = 2

    TIMESTAMP_INDEX = 0
    TIMESTAMP_STR_INDEX = 0
    TIMESTAMP_LATEST_INDEX = 1
    RESPONSE_INDEX = 1

    result = textwrap.fill("Showing responses for advisee with email " + bold(str(result_tuple[EMAIL_INDEX])) + " to field " + bold(str(result_tuple[FIELD_INDEX])), 80) + "\n\n"

    for response in result_tuple[RESPONSE_LIST_INDEX]:
        timestamp_tuple = response[TIMESTAMP_INDEX]
        timestamp_latest = timestamp_tuple[TIMESTAMP_LATEST_INDEX]
        timestamp = negative(str(timestamp_tuple[TIMESTAMP_STR_INDEX])) if timestamp_latest else str(timestamp_tuple[TIMESTAMP_STR_INDEX])
        response_string = str(response[RESPONSE_INDEX])
        result += timestamp + "\n" + textwrap.fill(response_string, width=80) + "\n"

    return result
