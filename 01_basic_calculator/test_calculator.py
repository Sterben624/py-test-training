from calculator import Calculator
import pytest

@pytest.fixture
def calculator():
    return Calculator()

def test_add(calculator):
    assert calculator.add(1, 2) == 3
    assert calculator.add(-1, 1) == 0
    assert calculator.add(-1, -1) == -2

def test_subtract(calculator):
    assert calculator.subtract(5, 3) == 2
    assert calculator.subtract(3, 5) == -2
    assert calculator.subtract(-1, -1) == 0

def test_multiply(calculator):
    assert calculator.multiply(2, 3) == 6
    assert calculator.multiply(-1, 1) == -1
    assert calculator.multiply(-2, -3) == 6

def test_divide(calculator):
    assert calculator.divide(6, 3) == 2
    assert calculator.divide(-6, 3) == -2
    assert calculator.divide(-6, -3) == 2
    with pytest.raises(ZeroDivisionError):
        calculator.divide(1, 0)

def test_power(calculator):
    assert calculator.power(2, 3) == 8
    assert calculator.power(5, 0) == 1
    assert calculator.power(2, -2) == 0.25

def test_square_root(calculator):
    assert calculator.square_root(4) == 2
    assert calculator.square_root(0) == 0
    with pytest.raises(ValueError):
        calculator.square_root(-1)
    assert calculator.square_root(25) == 5