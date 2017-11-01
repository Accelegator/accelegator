""" Returns string with an advisee's flattened responses. """
import textwrap
import logging
import display_search
from colors import bold
from colors import negative


def display_show(result_tuple):
    """ Returns string with an advisee's flattened responses. Input is in form: (email, [((timestamp, latest), field, response)]) """

    if not result_tuple:
        logging.error("No input tuple given")
        return "No responses to display"

    EMAIL_INDEX = 0
    RESPONSE_LIST_INDEX = 1

    TIMESTAMP_INDEX = 0
    TIMESTAMP_STR_INDEX = 0
    TIMESTAMP_LATEST_INDEX = 1
    FIELD_INDEX = 1
    RESPONSE_INDEX = 2

    result = textwrap.fill("Showing flattened responses for advisee with email " + bold(str(result_tuple[EMAIL_INDEX])), 80) + "\n"

    for response in result_tuple[RESPONSE_LIST_INDEX]:
        field = (str(response[FIELD_INDEX]))
        timestamp_tuple = response[TIMESTAMP_INDEX]
        timestamp_latest = timestamp_tuple[TIMESTAMP_LATEST_INDEX]
        timestamp = negative(str(timestamp_tuple[TIMESTAMP_STR_INDEX])) if timestamp_latest else str(timestamp_tuple[TIMESTAMP_STR_INDEX])
        response_string = str(response[RESPONSE_INDEX])
        result += display_search.align(field, timestamp) + "\n"

        result += textwrap.fill(response_string, width=80) + "\n"

    return result
