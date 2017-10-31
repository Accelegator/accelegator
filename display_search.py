""" Displays list of advisees with responses that match search query. """
# Implementation will be moved to display.py once completed

# external dependencies
from colors import negative
from colors import bold


def display_search(list_of_tuples, has_field=False):
    """ Returns string of all responses returned by search """
    TIMESTAMP_TUPLE_INDEX = 0
    TIMESTAMP_STRING_INDEX = 0
    TIMESTAMP_BOOLEAN_INDEX = 1
    KEYWORD_INDEX = 1
    EMAIL_INDEX = 2
    FIELD_INDEX = 3
    RESPONSE_INDEX = 4

    # using first response to get keyword and field (if has_field == True)
    FIRST_RESPONSE = list_of_tuples[0]
    KEYWORD = bold(FIRST_RESPONSE[KEYWORD_INDEX])
    FIELD = bold(FIRST_RESPONSE[FIELD_INDEX])
    result = "Displaying search results for keyword " + KEYWORD + " in field " + FIELD + "\n\n" if has_field else "Displaying search results for keyword " + KEYWORD + "\n\n"

    for response in list_of_tuples:
        # if timestamp is latest, invert the colors
        timestamp_tuple = response[TIMESTAMP_TUPLE_INDEX]
        timestamp_boolean = timestamp_tuple[TIMESTAMP_BOOLEAN_INDEX]
        # if timestamp is latest, invert its color
        timestamp = negative(timestamp_tuple[TIMESTAMP_STRING_INDEX]) if timestamp_boolean else timestamp_tuple[TIMESTAMP_STRING_INDEX]

        response_string = align(response[EMAIL_INDEX], timestamp, timestamp_boolean) + "\n" + response[FIELD_INDEX] + "\n" + response[RESPONSE_INDEX] + "\n\n"
        result += response_string

    return result


def align(left, right, is_negative_timestamp=False):
    """ Returns string with "left" aligned to the left and "right" aligned to the right """
    if is_negative_timestamp:
        # adjust right alignment for ansi sequence of inverted timestamp
        return "{:<40s}{:>48s}".format(left, right)
    else:
        return "{:<40s}{:>40s}".format(left, right)