""" Displays an advisee's flattened responses. """
import textwrap
import logging
from colors import bold
from colors import negative


def display_show_with_field(tuple_of_tuples):
	""" Displays an advisee's flattened responses. """
	
	#immediately leaves if the output is None
	if not tuple_of_tuples:
		logging.error("No input was found for tuple_of_tuples")
		return "No responses to display"
		
	#input for display_show_with_feild
	"""`show <email> <field>` --- `(email, field, [((timestamp, latest), response)])`"""
	
	#CONSTANTS
	EMAIL_INDEX = 0
	RESPONSE_LIST = 2
	FIELD_INDEX = 1 
	RESPONSE_INDEX = 1
	TIMESTAMP_INDEX = 0
	TIMESTAMP_STR_INDEX = 0
	TIMESTAMP_BOOL_INDEX = 1

	field_str = ""
	timestamp_str= ""
	string_tuple_of_tuples = ""
	
	initial_string = textwrap.fill("Displaying " + result_tuple[EMAIL_INDEX] + "'s results for: " + result_tuple[FIELD_INDEX], 80)
	initial_string += "\n\n"
	
	string_result_tuple = initial_string
	
	#iterates through RESPONSE_LIST
	for tuple in result_tuple[RESPONSE_LIST]:

		timestamp_tuple = tuple[TIMESTAMP_INDEX]
		timestamp_str = str(timestamp_tuple[TIMESTAMP_STR_INDEX])
		
		if timestamp_tuple[TIMESTAMP_BOOL_INDEX]:
			timestamp_str = negative(timestamp_str)
	
		string_result_tuple += timestamp_str
		string_result_tuple +="\n"
		
		#no alignment needed for the RESPONSE
		#textwrap.fill(<data>, 80) will wrap the text in lines of 80 characters.
		string_result_tuple += (textwrap.fill(str(tuple[RESPONSE_INDEX]), 80))
		string_result_tuple += "\n \n"
		
	return string_result_tuple