""" tests for the various query functions """


from io import StringIO
import pandas
import queries


CSVDATA = StringIO("""timestampcol, emailcol, field1col, field2col
asdf, fdsa, hgfd, dfhg
qwer, rewq, uytr, rtyu
poiu, uiop, lkjh, jkkj""")

DATAFRAME = pandas.read_csv(CSVDATA)


def test_query_search_matches():
    """ verify query_search returns matches correctly """
    actual = queries.query_search(DATAFRAME, "qwer")
    expected = ('qwer', [(('qwer', True), ' rewq', 'timestampcol', 'qwer')])
    assert actual == expected


def test_query_search_no_matches():
    """ verify query_search behaves correctly when no matches exist """
    actual = queries.query_search(DATAFRAME, "nope")
    expected = ('nope', [])
    assert actual == expected


def test_query_search_field():
    """ verify query_search_field restricts the match domain """


def test_query_show_field():
    """ verify single field with historical data is returned """


def test_query_show():
    """ verify all fields for given student are returned """


def test_query_list():
    """ verify all students are returned, identified by email """
