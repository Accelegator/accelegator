""" Displays an advisee's flattened responses. """
import textwrap
import logging
from display_search import align
from colors import bold
from colors import negative


def display_show(result_tuple):


	#immediately leaves if the output is None
	if not result_tuple:
		logging.error("No input was found for tuple_of_tuples")
		return "No responses to display"
		
	#input for display_show
	"""`show <email>` --- `(email, [((timestamp, latest), field, response)])`"""
	
	#CONSTANTS
	EMAIL_INDEX = 0
	RESPONSE_LIST = 1
	FIELD_INDEX = 1
	RESPONSE_INDEX = 2
	TIMESTAMP_INDEX = 0
	TIMESTAMP_STR_INDEX = 0
	TIMESTAMP_BOOL_INDEX = 1

	field_str = ""
	timestamp_str= ""
	string_result_tuple = ""
	
	initial_string = textwrap.fill("Showing all results for: " + str(result_tuple[EMAIL_INDEX]), 80)
	initial_string += "\n\n"
	
	string_tuple_of_tuples = initial_string
	
	#iterates through RESPONSE_LIST
	for tuple in result_tuple[RESPONSE_LIST]:
		field_str = (str(tuple[FIELD_INDEX]))
		timestamp_tuple = tuple[TIMESTAMP_INDEX]
		timestamp_str = str(timestamp_tuple[TIMESTAMP_STR_INDEX])
		
		if timestamp_tuple[TIMESTAMP_BOOL_INDEX]:
			timestamp_str = negative(timestamp_str)
		
		#align function will align text to the right and left side of the terminal
		string_result_tuple += align(field_str, timestamp_str)
		string_result_tuple +="\n"
		
		#no alignment needed for the RESPONSE
		#textwrap.fill(<data>, 80) will wrap the text in lines of 80 characters.		
		string_result_tuple += (textwrap.fill(str(tuple[RESPONSE_INDEX]), 80))
		string_result_tuple += "\n \n"
		
	return string_result_tuple