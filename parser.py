""" parses the CSV from spreadsheet.py into a sqlite database """

import logging
import pandas


def parse_csv_into_dataframe(filepath):
    """ parses csv file into an in-memory sqlite database """
    dataframe = pandas.read_csv(filepath)
    logging.debug("generated pandas dataframe:")
    logging.debug(dataframe)
    return dataframe
