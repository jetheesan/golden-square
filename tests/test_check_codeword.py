from lib.check_codeword import *

def test_codeword_is_horse():
    result = check_codeword("horse")
    assert result == "Correct! Come in."


def test_codeword_is_starts_with_h_and_ends_in_e():
    result = check_codeword("here")
    assert result == "Close, but nope."
    result = check_codeword("home")
    assert result == "Close, but nope."

def test_codeword_is_not_close():
    result = check_codeword("abcdefg")
    assert result == "WRONG!"