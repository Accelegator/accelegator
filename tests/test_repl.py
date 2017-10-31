import repl

def test_repl_1():
    assert repl("list") == 0

def test_repl_2():
    assert repl("show", "email") == 1

def test_repl_3():
    assert repl("show", "email", "name") == 2

def test_repl_4():
    assert repl("search", "email") == 3

def test_repl_5():
    assert repl("search", "email", "name") == 4

def test_repl_6():
    assert repl("help") == 5

def test_repl_7():
    assert repl("help", "command") == 6
