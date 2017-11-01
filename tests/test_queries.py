""" tests for the various query functions """


from io import StringIO
import pandas
import queries


CSVDATA = StringIO("""timestampcol,emailcol,field1col,field2col
asdf,fdsa,hgfd,dfhg
qwer,rewq,uytr,rtyu
poiu,uiop,lkjh,jkkj""")

DATAFRAME = pandas.read_csv(CSVDATA)


def test_query_search_matches():
    """ verify query_search returns matches correctly """
    actual = queries.query_search(DATAFRAME, "qwer")
    expected = ('qwer', [(('qwer', True), 'rewq', 'timestampcol', 'qwer')])
    assert actual == expected


def test_query_search_matches2():
    """ verify query_search returns matches correctly """
    actual = queries.query_search(DATAFRAME, "rty")
    expected = ('rty', [(('qwer', True), 'rewq', 'field2col', 'rtyu')])
    assert actual == expected


def test_query_search_no_matches():
    """ verify query_search behaves correctly when no matches exist """
    actual = queries.query_search(DATAFRAME, "nope")
    expected = ('nope', [])
    assert actual == expected


def test_query_search_field_matches():
    """ verify query_search_field behaves correctly when matches exist """
    actual = queries.query_search_field(DATAFRAME, 3, "jkk")
    expected = ('jkk', 3, [(('poiu', True), 'uiop', 'jkkj')])
    assert actual == expected


def test_query_search_field_nomatch():
    """ verify query_search_field behaves correctly when no matches exist """
    actual = queries.query_search_field(DATAFRAME, 3, "uytr")
    expected = ('uytr', 3, [])
    assert actual == expected


def test_query_show_field():
    """ verify single field with historical data is returned """
    actual = queries.query_show_field(DATAFRAME, 3, "rewq")
    expected = ("rewq", "field2col", [(("qwer", True), "rtyu")])
    assert actual == expected


def test_query_show():
    """ verify all fields for given student are returned """
    actual = queries.query_show(DATAFRAME, "rewq")
    expected = ("rewq", [
        (("qwer", True), "timestampcol", "qwer"),
        (("qwer", True), "emailcol", "rewq"),
        (("qwer", True), "field1col", "uytr"),
        (("qwer", True), "field2col", "rtyu")])
    assert actual == expected


def test_query_list():
    """ verify all students are returned, identified by email """
    actual = queries.query_list(DATAFRAME)
    expected = ["fdsa", "rewq", "uiop"]
    assert actual == expected
