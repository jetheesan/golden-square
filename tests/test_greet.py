from lib.greet import *

def test_for_john():
    result = greet("John")
    assert result == "Hello, John"