""" queries supporting the different user commands """

import logging

def query_list():
    """ returns list of emails of the advisees that have responded """
    # return type should be a list of strings

def query_show(short_email):
    """ returns latest responses for each field for the given student """
    # return type should be a list of tuples
    # each tuple having format (date, latest, field)

def query_show_field(field, short_email):
    """ returns all historical responses for the given field and student """
    # return type should be a list of tuples
    # each tuple having format (date, field)
    # sorted such that most recent comes last

def query_search(keyword):
    """ returns dataframe rows containing the keyword """
    # return type should be a list of tuples
    # each tuple having format (email, field_name, field_content)

def query_search_field(field, keyword):
    """ returns dataframe rows where the field contains the keyword """
    # return type should be a list of tuples
    # each tuple having format (email, field_name, field_content)

def determine_latest(short_email, date, field):
    """ returns true if given field is the latest response """
    # return type should be boolean
