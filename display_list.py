""" Returns a string that is list of advisees. """

# Implementation will be moved to display.py once completed
from colors import bold


def display_list(list_of_advisees):
    """ Returns a string that is list of advisees' emails """
    result = bold("Advisees") + "\n"

    if not list_of_advisees or list_of_advisees is None:
        return result + "None to list\n"

    for email in list_of_advisees:
        result += str(email) + "\n"

    return result
