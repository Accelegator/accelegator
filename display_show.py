""" Displays an advisee's flattened responses. """
import textwrap
# Implementation will be moved to display.py once completed
def display_show(tuple_of_tuples):

	#these constants control which portion of the tuple come first
	field = 1
	timestamp = 0
	response = 2
	string_tuple_of_tuples = ""
	
	#for each tuple in the tuple of tuples, we'll print out the field, timestamp, and the response given
	for tuple in tuple_of_tuples:
		#textwrap.fill(<data>, 80) will wrap the text in lines of 80 characters.
		string_tuple_of_tuples+=(textwrap.fill(str(tuple[field]), 80))
		string_tuple_of_tuples+=(textwrap.fill(str(tuple[timestamp]), 80))
		string_tuple_of_tuples+=(textwrap.fill(str(tuple[response]), 80))
		return string_tuple_of_tuples
		
		
tuple_of_tuples = (("timestamp", "id", "12345"), ("timestamp", "email", "maria@maria.com"))
print(display_show(tuple_of_tuples))