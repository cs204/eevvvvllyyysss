import pytest
from bank import value

def test_value_greeting_hello():
    assert value("Здравствуйте") == 0

def test_value_greeting_z():
    assert value("Здрасте") == 20

def test_value_greeting_other():
    assert value("Привет") == 100

def test_value_greeting_empty():
    assert value("") == 100

def test_value_greeting_lowercase():
    assert value("здравствуйте") == 0
    assert value("з") == 20
    assert value("привет") == 100
