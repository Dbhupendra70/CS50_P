from bank import value


def test_value_0():
    assert value("Hello, Newman ")==0

def test_value_10():
    assert value("How are you doing?")== 20

def test_value_100():
    assert value("What's happening?")== 100


