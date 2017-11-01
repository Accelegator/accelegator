""" Test functions for REPL """

import repl


def test_repl_1():
    """ Test list """
    assert repl.repl("list", "", "", "", "data") == 0


def test_repl_2():
    """ Test show with keyword """
    assert repl.repl("show","email", "", "", "data") == 1


def test_repl_3():
    """ Test show with two keywords """
    assert repl.repl("show", "email", "name", "", "data") == 2


def test_repl_4():
    """ Test search with keyword """
    assert repl.repl("search", "email", "", "", "data") == 3


def test_repl_5():
    """ Test search with two keywords """
    assert repl.repl("search", "email", "name", "", "data") == 4


def test_repl_6():
    """ Test help """
    assert repl.repl("help", "", "", "", "") == 5


def test_repl_7():
    """ Test help with command """
    assert repl.repl("help", "list", "", "", "") == 6


def test_repl_8():
    """ Test write list """
    assert repl.repl("write", "list", "", "", "data") == 7


def test_repl_9():
    """ Test write show with keyword """
    assert repl.repl("write", "show", "email", "", "data") == 8


def test_repl_10():
    """ Test write show with two keywords """
    assert repl.repl("write", "show", "email", "name", "data") == 9


def test_repl_11():
    """ Test write search with keyword """
    assert repl.repl("write", "search", "email", "", "data") == 10


def test_repl_12():
    """ Test write search with two keywords """
    assert repl.repl("write", "search", "email", "name", "data") == 11
