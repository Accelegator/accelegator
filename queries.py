""" queries supporting the different user commands """

import logging
import pandas


EMAIL_INDEX = 1
TIMESTAMP_INDEX = 0


def parse_csv_into_dataframe(filepath):
    """ parses csv file into an pandas dataframe """
    dataframe = pandas.read_csv(filepath)
    logging.debug("generated pandas dataframe:")
    logging.debug(dataframe)
    return dataframe


def _determine_latest(dataframe, email, date, field_index):
    """ returns true if given field is the latest response """
    return True # FIXME
    # return: true/false


def query_list(dataframe):
    """ returns list of emails of the advisees that have responded """
    # return: [email, email, ...]


def query_show(dataframe, email):
    """ returns latest responses for each field for the given student """
    # return: (email, [((timestamp, latest), field, response)])


def query_show_field(dataframe, field, email):
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
                _datetime = dataframe.iat[rowindex, TIMESTAMP_INDEX]
                _latest = _determine_latest(dataframe, email,
                                            _datetime, colindex)
                timestamp = (_datetime, _latest)
                retlist.append((timestamp, email, field, response))
                break  # stop matching against this row early
    return (keyword, retlist)
    # return: (keyword, [((timestamp, latest), email, field, response)])


def query_search_field(dataframe, field, keyword):
    """ returns dataframe rows where the field contains the keyword """
    logging.debug("query_search_field: " + keyword + field)
    trimmed_frame = dataframe.iloc[:, [EMAIL_INDEX, TIMESTAMP_INDEX, field]]
    (_, retlist) = query_search(trimmed_frame, keyword)
    return (keyword, field, retlist)
    # return: (keyword, field, [((timestamp, latest), email, response)])
