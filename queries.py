""" queries supporting the different user commands """

import logging


def query_list(dataframe):
    """ returns list of emails of the advisees that have responded """
    # return type should be a list of strings


def query_show(dataframe, short_email):
    """ returns latest responses for each field for the given student """
    logging.debug("query_show: " + email)
    retlist = []
    
    (row, cols) = dataframe.shape
    for rowindex in range(0, rows):
        for colindex in range(0, cols):
             if keyword in str(dataframe.iat[rowindex, colindex]):

                    email = dataframe.iat[rowindex, EMAIL_INDEX]
                    field = dataframe.iat[0, colindex]
                    response = dataframe.iat[rowindex, TIMESTAMP_INDEX]
                    latest = _determine_latest(dataframe, email, timestamp, colindex)
                    timestamp = (datatime, latest)

                    retlist.append((timestamp, email, field, response
                    break
    return (email, retlist)
    # return: [((timestamp, latest), email, date, latest, field)]
    # return type should be a list of tuples
    # each tuple having format (date, latest, field)


def query_show_field(dataframe, field, short_email):
    """ returns all historical responses for the given field and student """
    logging.debug("query_show_field: " + field + email)
    
    (_, retlist) = query_search(dataframe, field, email)
    return (keyword, field, retlist)
    # return type should be a list of tuples
    # each tuple having format (date, field)
    # sorted such that most recent comes last


def query_search(dataframe, keyword):
    """ returns dataframe rows containing the keyword """
    # return type should be a list of tuples
    # each tuple having format (email, field_name, field_content)


def query_search_field(dataframe, field, keyword):
    """ returns dataframe rows where the field contains the keyword """
    # return type should be a list of tuples
    # each tuple having format (email, field_name, field_content)


def determine_latest(dataframe, short_email, date, field):
    """ returns true if given field is the latest response """
    # return type should be boolean
