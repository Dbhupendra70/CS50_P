from plates import is_valid


# “All vanity plates must start with at least two letters.”
def test_TwoLetters():
    assert is_valid("CS") == True
    assert is_valid("CS50") == True
    assert is_valid("50") == False
    assert is_valid("C50P") == False


# “… vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.”
def test_6letters():
    assert is_valid("CSE333") == True
    assert is_valid("CS50") == True
    assert is_valid("CSP1234") == False

# “Numbers cannot be used in the middle of a plate; they must come at the end. For example, AAA222 would be an acceptable … vanity plate; AAA22A would not be acceptable. The first number used cannot be a ‘0’.”
def test_num():
    assert is_valid("AAA222") == True
    assert is_valid("BBB022") == False
    assert is_valid("CCC33A") == False


# “No periods, spaces, or punctuation marks are allowed.”
def test_punch():
    assert is_valid("CS50") == True
    assert is_valid("HICS50") == True
    assert is_valid("AAA2!") == False
