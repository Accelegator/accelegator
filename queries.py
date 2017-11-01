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
    # logging.debug("determine_latest: " + email + date + field)
    # (rows, _) = dataframe.shape
    # for rowindex in range(0, rows):
    #     if short_email == dataframe.iat[rowindex, EMAIL_INDEX]:
    #         if dataframe.iat[dataframe, TIMESTAMP_INDEX] >= date
    #             return False
    return True
    # FIXME >> broken.


def query_list(dataframe):
    """ returns list of emails of the advisees that have responded """
    logging.debug("query_list")
    retlist = []
    (rows, _) = dataframe.shape
    for rowindex in range(0, rows):
        if dataframe.iat[rowindex, EMAIL_INDEX] not in retlist:
            retlist.append(dataframe.iat[rowindex, EMAIL_INDEX])
    return retlist
    # return: [email, email, ...]


def query_show(dataframe, email):
    """ returns latest responses for each field for the given student """
    logging.debug("query_show: " + email)
    retlist = []
    (rows, cols) = dataframe.shape
    for rowindex in range(0, rows):
        if dataframe.iat[rowindex, EMAIL_INDEX] == email:
            retlist = []
            for colindex in range(0, cols):
                field = dataframe.columns[colindex]
                response = dataframe.iat[rowindex, colindex]
                _datetime = dataframe.iat[rowindex, TIMESTAMP_INDEX]
                _latest = _determine_latest(dataframe, email,
                                            _datetime, colindex)
                timestamp = (_datetime, _latest)
                retlist.append((timestamp, field, response))
    return (email, retlist)
    # return: (email, [((timestamp, latest), field, response)])
    # FIXME >> should take into account blank/null responses and only return
    # the latest not-blank/not-null ones for each question/field -- currently
    # it just assumes all responses were required/mandatory, and assumes the
    # responses are in temporal sorted order as they are on the Google Sheet.


def query_show_field(dataframe, field, email):
    """ returns all historical responses for the given field and student """
    logging.debug("query_show_field: " + str(field) + email)
    response_list = []
    (rows, _) = dataframe.shape
    for rowindex in range(0, rows):
        if dataframe.iat[rowindex, EMAIL_INDEX] == email:
            response = dataframe.iat[rowindex, field]
            _datetime = dataframe.iat[rowindex, TIMESTAMP_INDEX]
            _latest = _determine_latest(dataframe, email,
                                        _datetime, field)
            timestamp = (_datetime, _latest)
            response_list.append((timestamp, response))
    field = dataframe.columns[field]
    return (email, field, response_list)
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
                field = dataframe.columns[colindex]
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
    logging.debug("query_search_field: " + keyword + str(field))
    trimmed_frame = dataframe.iloc[:, [TIMESTAMP_INDEX, EMAIL_INDEX, field]]
    (_, retlist) = query_search(trimmed_frame, keyword)
    returnlist = []
    for ret in retlist:
        (timestamp, email, _, response) = ret
        returnlist.append((timestamp, email, response))
    return (keyword, field, returnlist)
    # return: (keyword, field, [((timestamp, latest), email, response)])
