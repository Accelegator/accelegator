""" Displays an advisee's flattened responses. """
import textwrap
import logging
from display_search import align
from colors import bold


def display_show(tuple_of_tuples, has_field = False):


	#immediately leaves if the output is None
	if not tuple_of_tuples:
		logging.error("No input was found for tuple_of_tuples")
		return "No responses to display"

	#CONSTANTS
	FIELD = 1
	TIMESTAMP = tuple_of_tuples[2][0][0]
	RESPONSE = tuple_of_tuples[2][1]
	EMAIL_INDEX = 2
	
	FIRST_RESPONSE = tuple_of_tuples[2][1]
	EMAIL_FIELD = tuple_of_tuples[0]
	FIELD_TYPE = bold(FIRST_RESPONSE[FIELD])
	
	field_str = ""
	timestamp_str= ""
	string_tuple_of_tuples = ""
	
	if has_field:
		initial_string = textwrap.fill("Displaying " + EMAIL_FIELD + "'s results for: " + FIELD_TYPE, 80)
		initial_string += "\n\n"
	else:
		initial_string = textwrap.fill("Showing all results for: " + EMAIL_FIELD, 80)
		initial_string += "\n\n"
	
	string_tuple_of_tuples = initial_string
	
	"""Message for code inheriter"""
	#TODO: Change logic to match new input format:  (email, field, [((timestamp, latest), response)])
	#Reference: Old input looked like this (("timestamp", "field", "response"), ("timestamp", "field", "response")
	
	for tuple in tuple_of_tuples:
		#textwrap.fill(<data>, 80) will wrap the text in lines of 80 characters.
		field_str = (str(tuple[FIELD]))
		timestamp_str = (str(tuple[TIMESTAMP]))
		
		#align function will align text to the right and left side of the terminal
		string_tuple_of_tuples += align(field_str, timestamp_str)
		string_tuple_of_tuples+="\n"
		
		#no alignment needed for the RESPONSE
		string_tuple_of_tuples+=(textwrap.fill(str(tuple[RESPONSE]), 80))
		string_tuple_of_tuples+="\n \n"
		
	return string_tuple_of_tuples