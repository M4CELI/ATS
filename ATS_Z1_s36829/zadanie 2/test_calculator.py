import pytest
from calculator import Calculator


@pytest.mark.parametrize("a, b, op, expected", [
    (2, 3, "+", 5),
    (10, 4, "-", 6),
    (3, 4, "*", 12),
    (10, 4, "/", 2.5),
    (-2, -3, "+", -5),
    (-2, 3, "*", -6),
    (0, 5, "*", 0),
    (0, 5, "/", 0),
    (1e10, 1e10, "+", 2e10),
])
def test_basic_operations(a, b, op, expected):
    assert Calculator(a, b, op).calculate() == pytest.approx(expected)


def test_float_precision():
    assert Calculator(0.1, 0.2, "+").calculate() == pytest.approx(0.3)


def test_division_by_zero():
    with pytest.raises(ZeroDivisionError):
        Calculator(5, 0, "/").calculate()


@pytest.mark.parametrize("op", ["%", "^", "", "plus", None])
def test_invalid_operator(op):
    with pytest.raises(ValueError):
        Calculator(1, 2, op)


@pytest.mark.parametrize("a, b", [("1", 2), (1, None), (True, 2), ([1], 2)])
def test_invalid_operands(a, b):
    with pytest.raises(TypeError):
        Calculator(a, b, "+")


def test_operands_stored():
    calc = Calculator(7, 8, "-")
    assert (calc.a, calc.b, calc.op) == (7, 8, "-")