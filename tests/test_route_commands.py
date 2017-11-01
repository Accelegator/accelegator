""" Test functions for route_commands """

import route_commands


def test_route_commands_1():
    """ Test list """
    assert route_commands.route_commands("list", "", "", "") == 1


def test_route_commands_2():
    """ Test show with keyword """
    assert route_commands.route_commands("show", "email", "", "") == 2


def test_route_commands_3():
    """ Test show with two keywords """
    assert route_commands.route_commands("show", "email", "name", "") == 3


def test_route_commands_4():
    """ Test search with keyword """
    assert route_commands.route_commands("search", "email", "", "") == 4


def test_route_commands_5():
    """ Test search with two keywords """
    assert route_commands.route_commands("search", "email", "name", "") == 5


def test_route_commands_8():
    """ Test write list """
    assert route_commands.route_commands("write", "list", "", "") == 6


def test_route_commands_9():
    """ Test write show with keyword """
    assert route_commands.route_commands("write", "show", "email", "") == 7


def test_route_commands_10():
    """ Test write show with two keywords """
    assert route_commands.route_commands("write", "show", "email", "name") == 8


def test_route_commands_11():
    """ Test write search with keyword """
    assert route_commands.route_commands("write", "search", "email", "") == 9


def test_route_commands_12():
    """ Test write search with two keywords """
    assert route_commands.route_commands("write", "search", "email", "name") == 10


def test_route_commands_6():
    """ Test help """
    assert route_commands.route_commands("help", "", "", "") == 11


def test_route_commands_7():
    """ Test help with command """
    assert route_commands.route_commands("help", "list", "", "") == 12
