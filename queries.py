""" queries supporting the different user commands """

import logging
import pandas


EMAIL_INDEX=1
TIMESTAMP_INDEX=0


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
    (rows, cols) = dataframe.shape
    for rowindex in range(0, rows):
        for colindex in range(0, cols):
            if keyword in str(dataframe.iat[rowindex, colindex]):

                email = dataframe.iat[rowindex, EMAIL_INDEX]
                field = dataframe.iat[0, colindex]
                response = dataframe.iat[rowindex, colindex]
                datetime = dataframe.iat[rowindex, TIMESTAMP_INDEX]
                latest = _determine_latest(dataframe, email, timestamp, colindex)
                timestamp = (datetime, latest)

                retlist.append((timestamp, email, field, response))
                break  # stop matching against this row early
    return (keyword, retlist)
    # return: (keyword, [((timestamp, latest), email, field, response)])


def query_search_field(dataframe, field, keyword):
    """ returns dataframe rows where the field contains the keyword """
    logging.debug("query_search_field: " + keyword + field)

    # FIXME: trim away the unneeded parts dataframe, without modifying the source
    # (select EMAIL_INDEX column, field column, TIMESTAMP_INDEX column)

    (_, retlist) = query_search(dataframe, keyword)
    return (keyword, field, retlist)
    # return: (keyword, field, [((timestamp, latest), email, response)])
