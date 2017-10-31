from display_show import display_show
from display_show import align
from colors import bold

def test_display_show():
	"""checks that display_show will properly output information"""
	tuple_of_tuples = ("Aug 03 00:00:35 2010", "email", "honokak@otonokizaka.edu")
	string_of_tuples = display_show(tuple_of_tuples)
	assert string_of_tuples = "Showing all results for: \x1b[1mhonokak@otonokizaka.edu\x1b[0m" + "\n\n" + align("email", "Aug 03 00:00:35 2010") + "\n" + textwrap.fill("honokak@otonokizaka.edu"), 80)
	
def test_align():
    """ Checks that align() returns properly aligned string """
    aligned = align("honokak@otonokizaka.edu", "Aug 03 00:00:35 2010")
    assert len(aligned) == 80
	

