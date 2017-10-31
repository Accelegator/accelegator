""" Accelegator: A Software Tool for Accelerated and Adaptive Advising """

# python libraries
import sys

# local dependencies
from parser import parse_csv_into_dataframe
from parse_arguments import parse_arguments
import display_strings
from defaults import DEFAULT_CSVFILE
from spreadsheet import create_csv

if __name__ == '__main__':

    ARGUMENTS = parse_arguments(sys.argv[1:])
    print(display_strings.WELCOME)
    create_csv()

    # FIXME >> should match CSV filepath written from spreadsheet.py
    DATAFRAME = parse_csv_into_dataframe(DEFAULT_CSVFILE)
