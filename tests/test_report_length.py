from lib.report_length import *

def test_for_three_letter_word():
    result = report_length("the")
    assert result == "This string was 3 characters long."

def test_for_four_letter_word():
    result = report_length("then")
    assert result == "This string was 4 characters long."