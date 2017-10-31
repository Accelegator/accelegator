""" queries supporting the different user commands """

import logging
import pandas


def parse_csv_into_dataframe(filepath):
    """ parses csv file into an pandas dataframe """
    dataframe = pandas.read_csv(filepath)
    logging.debug("generated pandas dataframe:")
    logging.debug(dataframe)
    return dataframe


def _determine_latest(dataframe, short_email, date, field):
    """ returns true if given field is the latest response """
    return True # FIXME
    # return: true/false


def query_list(dataframe):
    """ returns list of emails of the advisees that have responded """
    # return: [email, email, ...]


def query_show(dataframe, short_email):
    """ returns latest responses for each field for the given student """
    # return: (email, [((timestamp, latest), field, response)])


def query_show_field(dataframe, field, short_email):
    """ returns all historical responses for the given field and student """
    # return: (email, field, [((timestamp, latest), response)])


def query_search(dataframe, keyword):
    """ returns dataframe rows containing the keyword """
    logging.debug("query_search: " + keyword)
    retlist = []

    # FIXME: go through the entries in the dataframe
    # FIXME: append those containing keyword to the retlist
    # FIXME: in the specific format required

    return (keyword, retlist)
    # return: (keyword, [((timestamp, latest), email, field, response)])


def query_search_field(dataframe, field, keyword):
    """ returns dataframe rows where the field contains the keyword """
    logging.debug("query_search_field: " + keyword + field)

    # FIXME: trim away the unneeded parts dataframe, without modifying the source

    (_, retlist) = query_search(dataframe, keyword)
    return (keyword, field, retlist)
    # return: (keyword, field, [((timestamp, latest), email, response)])
