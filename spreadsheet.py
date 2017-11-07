""" Creates a csv file from the Google Form after collection of data """

import csv
import logging
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from defaults import DEFAULT_CSVFILE
from defaults import DEFAULT_WORKBOOK


def create_csv():
    """ Pulls data from Google Sheets, writing to the default CSV file """

    file_name = "./" + DEFAULT_CSVFILE
    logging.info("Authenticating to Google Sheets to obtain Google Form data")
    # use creds to create a client to interact with the Google Drive API
    scope = ['https://spreadsheets.google.com/feeds']
    creds = ServiceAccountCredentials.from_json_keyfile_name(
        'AGAuthKey.json', scope)
    client = gspread.authorize(creds)

    # Find a workbook by name and open the first sheet
    # Make sure you use the right name here.
    sheet = client.open(DEFAULT_WORKBOOK).sheet1

    # Extract and print all of the values
    list_of_hashes = sheet.get_all_values()

    logging.info("Writing formatted data to CSV file")
    logging.debug("CSV file name: " + file_name)
    with open(file_name, 'w') as myfile:
        writer = csv.writer(myfile, quoting=csv.QUOTE_ALL)
        for ha in list_of_hashes:
            writer.writerow(ha)
