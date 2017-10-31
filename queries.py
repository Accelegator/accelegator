""" queries supporting the different user commands """

import logging
import pandas


def query_list(dataframe):
    """ returns list of emails of the advisees that have responded """
    # return: [email, email, ...]


def query_show(dataframe, short_email):
    """ returns latest responses for each field for the given student """
    # return: (email, [((timestamp, latest), field, response)])


def query_show_field(dataframe, field, short_email):
    """ returns all historical responses for the given field and student """
    # return: (email, field, [((timestamp, latest), response)])
    # sorted: most recent comes last


def query_search(dataframe, keyword):
    """ returns dataframe rows containing the keyword """
    # return: (keyword, [((timestamp, latest), email, field, response)])


def query_search_field(dataframe, field, keyword):
    """ returns dataframe rows where the field contains the keyword """
    # return: (keyword, field, [((timestamp, latest), email, response)])


def determine_latest(dataframe, short_email, date, field):
    """ returns true if given field is the latest response """
    # return: true/false
