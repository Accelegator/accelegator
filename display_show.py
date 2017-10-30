""" Displays an advisee's flattened responses. """
import textwrap
# Implementation will be moved to display.py once completed
def display_show(tuple_of_tuples):

	#these constants control which portion of the tuple come first
	field = 1
	timestamp = 0
	response = 2
	
	field_str = ""
	timestamp_str= ""
	string_tuple_of_tuples = ""
	
	#for each tuple in the tuple of tuples, we'll print out the field, timestamp, and the response given
	for tuple in tuple_of_tuples:
		#textwrap.fill(<data>, 80) will wrap the text in lines of 80 characters.
		field_str = (textwrap.fill(str(tuple[field]), 80))
		timestamp_str = (textwrap.fill(str(tuple[timestamp]), 80))
		#align function will align text to the right and left side of the terminal
		string_tuple_of_tuples += align(field_str, timestamp_str)
		string_tuple_of_tuples+="\n"
		#no alignment needed for the response
		string_tuple_of_tuples+=(textwrap.fill(str(tuple[response]), 80))
		string_tuple_of_tuples+="\n \n"
		
	return string_tuple_of_tuples
		

def align(left, right):
    """ Returns string with "left" aligned to the left and "right" aligned to the right """
    return "{:<38s}{:>38s}".format(left, right)
