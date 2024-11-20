from twttr import shorten

def test_shorten():
    assert shorten("Hello, World!") == "Hll, Wrld!"
    assert shorten("Goodbye!") == "Gdby!"
    assert shorten("1234") == "1234"
    assert shorten("This is a test.") == "Ths s  tst."
    assert shorten("CS50")=="CS50"
    assert shorten("What's your name?") == "Wht's yr nm?"
    assert shorten("COME ON")=="CM N"

