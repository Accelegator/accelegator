""" Test functions for REPL """

import repl

def test_repl_1():
    """ Test list """
    assert repl("list", "data") == 0

def test_repl_2():
    """ Test show with keyword """
    assert repl("show", "data", "email") == 1

def test_repl_3():
    """ Test show with two keywords """
    assert repl("show", "data", "email", "name") == 2

def test_repl_4():
    """ Test search with keyword """
    assert repl("search", "data", "email") == 3

def test_repl_5():
    """ Test search with two keywords """
    assert repl("search", "data", "email", "name") == 4

def test_repl_6():
    """ Test help """
    assert repl("help") == 5

def test_repl_7():
    """ Test help with command """
    assert repl("help", "command") == 6

def test_repl_8():
    """ Test write list """
    assert repl("write", "data", "list") == 7

def test_repl_9():
    """ Test write show with keyword """
    assert repl("write", "data", "show", "email") == 8

def test_repl_10():
    """ Test write show with two keywords """
    assert repl("write", "data", "show", "email", "name") == 9

def test_repl_11():
    """ Test write search with keyword """
    assert repl("write", "data", "search", "email") == 10

def test_repl_12():
    """ Test write search with two keywords """
    assert repl("write", "data", "search", "email", "name") == 11
