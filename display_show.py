""" Displays an advisee's flattened responses. """
import textwrap
from display_search import align
from colors import bold


def display_show(tuple_of_tuples, has_field = False):

	tuple_of_tuples = (("Aug 03 00:00:35 2010", "email", "honokak@otonokizaka.edu"), 
	("Apr 19 00:00:35 2010", "email", "nishikinom@otonokizaka.edu"),
	("Jul 22 00:00:35 2010", "email", "yazawan@otonokizaka.edu"))

	#CONSTANTS
	FIELD = 1
	TIMESTAMP = 0
	RESPONSE = 2
	EMAIL_INDEX = 2
	
	FIRST_RESPONSE = tuple_of_tuples[0]
	EMAIL_FIELD = bold(FIRST_RESPONSE[EMAIL_INDEX])
	FIELD_TYPE = bold(tuple_of_tuples[FIELD])
	
	field_str = ""
	timestamp_str= ""
	string_tuple_of_tuples = ""
	
	Initial_String = "Showing all results for: " + EMAIL_FEILD + "\n\n" if has_field else "Displaying " + EMAIL_FIELD + "'s results for: " + FIELD_TYPE + "\n\n"
	
	#for each tuple in the tuple of tuples, print's out the FIELD, TIMESTAMP, and the RESPONSE given
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

print(display_show())