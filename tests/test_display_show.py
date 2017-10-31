from display_show import display_show
from display_search import align


def test_display_show():
	"""checks that display_show will properly output information"""
	tuple_of_tuples = ("Aug 03 00:00:35 2010", "email", "honokak@otonokizaka.edu")
	string_of_tuples = display_show(tuple_of_tuples)
	assert repr(string_of_tuples) == repr("Showing all results for: " +  bold("honokak@otonokizaka.edu") + "\n\n" + align("email", "Aug 03 00:00:35 2010") + "\n" + "honokak@otonokizaka.edu")*/
	
def test_align():
    """ Checks that align() returns properly aligned string """
    aligned = align("honokak@otonokizaka.edu", "Aug 03 00:00:35 2010")
    assert len(aligned) == 80
	

