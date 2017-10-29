""" Displays an advisee's flattened responses. """
import textwrap
# Implementation will be moved to display.py once completed
def display_show(tuple_of_tuples):

	#for each tuple in the tuple of tuples, we'll print out the field, timestamp, and the response given
	for tuple in tuple_of_tuples:
		print(textwrap.fill(tuple[1]), textwrap.fill(tuple[0]))
		print(textwrap.fill(tuple[2]))
