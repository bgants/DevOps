"""
Test goes here

"""

from mylib.calculator import add, subtract, multiply, divide


def test_add():
    assert add(1, 2) == 3


# create a multiple test
def test_multiply():
    assert multiply(3, 4) == 12


# create a subtract test
def test_subtract():
    assert subtract(5, 2) == 3


# create a divide test
def test_divide():
    assert divide(10, 2) == 5
