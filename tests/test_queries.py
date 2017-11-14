""" tests for the various query functions """


from io import StringIO
import pandas
import queries


CSVDATA = StringIO(u"""timestampcol,emailcol,field1col,field2col
"10/18/2017 13:40:21",fdsa,hgfd,dfhg
"10/18/2017 13:43:18",rewq,uytr,rtyu
"10/31/2017 14:16:04",uiop,lkjh,jkkj""")

DATAFRAME = pandas.read_csv(CSVDATA)


def test_query_search_matches():
    """ verify query_search returns matches correctly """
    actual = queries.query_search(DATAFRAME, "43:18")
    expected = ('43:18', [(('10/18/2017 13:43:18', True), 'rewq',
                           'timestampcol', '10/18/2017 13:43:18')])
    assert actual == expected


def test_query_search_matches2():
    """ verify query_search returns matches correctly """
    actual = queries.query_search(DATAFRAME, "rty")
    expected = ('rty', [(('10/18/2017 13:43:18', True),
                         'rewq', 'field2col', 'rtyu')])
    assert actual == expected


def test_query_search_no_matches():
    """ verify query_search behaves correctly when no matches exist """
    actual = queries.query_search(DATAFRAME, "nope")
    expected = ('nope', [])
    assert actual == expected


def test_query_search_field_matches():
    """ verify query_search_field behaves correctly when matches exist """
    actual = queries.query_search_field(DATAFRAME, 3, "jkk")
    expected = ('jkk', 3, [(('10/31/2017 14:16:04', True), 'uiop', 'jkkj')])
    assert actual == expected


def test_query_search_field_nomatch():
    """ verify query_search_field behaves correctly when no matches exist """
    actual = queries.query_search_field(DATAFRAME, 3, "uytr")
    expected = ('uytr', 3, [])
    assert actual == expected


def test_query_show_field():
    """ verify single field with historical data is returned """
    actual = queries.query_show_field(DATAFRAME, "rewq", 4)
    expected = ("rewq", "field2col", [(("10/18/2017 13:43:18", True), "rtyu")])
    assert actual == expected


def test_query_show():
    """ verify all fields for given student are returned """
    actual = queries.query_show(DATAFRAME, "rewq")
    expected = ("rewq", [
        (("10/18/2017 13:43:18", True), "timestampcol", "10/18/2017 13:43:18"),
        (("10/18/2017 13:43:18", True), "emailcol", "rewq"),
        (("10/18/2017 13:43:18", True), "field1col", "uytr"),
        (("10/18/2017 13:43:18", True), "field2col", "rtyu")])
    assert actual == expected


def test_query_list():
    """ verify all students are returned, identified by email """
    actual = queries.query_list(DATAFRAME)
    expected = ["fdsa", "rewq", "uiop"]
    assert actual == expected
