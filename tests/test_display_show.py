from display_show import display_show
from display_search import align


def test_display_show():
	"""checks that display_show will properly output information"""
	result_tuple = ("email", [(("timestamp", False), "field", "response")])
	string_tuple = display_show(result_tuple)
	assert repr(string_tuple) == textwrap.fill("Showing all results for: " + "email", 80) + align("field", "timestamp") + "\n" + textwrap.fill(str("response"), 80) + "\n\n"
	
def test_empty_tuples():
	"""checks display_show's output if you input an empty tuple_of_tuples"""
	tuple_of_tuples = ()
	assert display_show(tuple_of_tuples) == "No responses to display"
	
def test_align():
    """ Checks that align() returns properly aligned string """
    aligned = align("honokak@otonokizaka.edu", "Aug 03 00:00:35 2010")
    assert len(aligned) == 80
	

