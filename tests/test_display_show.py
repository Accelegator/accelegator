from display_show import display_show
from display_show import align

def test_display_show():
	"""checks that display_show will properly output information"""
	tuple_of_tuples = (("Aug 03 00:00:35 2010", "email", "honokak@otonokizaka.edu"), 
	("Apr 19 00:00:35 2010", "email", "nishikinom@otonokizaka.edu"),
	("Jul 22 00:00:35 2010", "email", "yazawan@otonokizaka.edu"))
	string_of_tuples = display_show(tuple_of_tuples)
	
def test_align():
    """ Checks that align() returns properly aligned string """
    aligned = align("honokak@otonokizaka.edu", "Aug 03 00:00:35 2010")
    assert len(aligned) == 80
	

