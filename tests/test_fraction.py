import pytest

from problem_solving_wads.fraction import Fraction


@pytest.mark.parametrize(
    ("f", "result"),
    (
        (Fraction(4, 5), "4/5"),
        (Fraction(5, 5), "1"),
        (Fraction(10, 5), "2"),
        (Fraction(-10, 5), "-2"),
    ),
)
def test_fraction_string(f: Fraction, result: str):
    assert str(f) == result


@pytest.mark.parametrize(
    ("f", "result"),
    (
        (Fraction(4, 5), "<Fraction: 4/5>"),
        (Fraction(5, 5), "<Fraction: 1>"),
        (Fraction(10, 5), "<Fraction: 2>"),
        (Fraction(-10, 5), "<Fraction: -2>"),
    ),
)
def test_fraction_repr(f: Fraction, result: str):
    assert repr(f) == result


@pytest.mark.parametrize(
    ("f1", "f2"),
    (
        (Fraction(4, 5), Fraction(4, 5)),
        (Fraction(5, 5), Fraction(3, 3)),
        (Fraction(10, 5), Fraction(30, 15)),
        (Fraction(-10, 5), Fraction(-30, 15)),
    ),
)
def test_fraction_eq(f1: Fraction, f2: Fraction):
    assert f1 == f2


@pytest.mark.parametrize(
    ("f1", "f2", "resultado"),
    (
        (Fraction(3, 4), Fraction(1, 4), Fraction(1)),
        (Fraction(2, 8), Fraction(3, 6), Fraction(3, 4)),
    ),
)
def test_fraction_add(f1: Fraction, f2: Fraction, resultado: Fraction):
    assert f1 + f2 == resultado


def test_fraction_iadd():
    f = Fraction(1, 4)
    f += Fraction(3, 4)
    assert f == Fraction(1)


@pytest.mark.parametrize(
    ("f1", "f2", "result"),
    (
        (Fraction(1, 2), Fraction(2, 5), Fraction(1, 5)),
        (Fraction(3, 6), Fraction(6, 7), Fraction(3, 7)),
        (Fraction(-5, 10), Fraction(4, 8), Fraction(-1, 4)),
        (Fraction(5, -10), Fraction(4, 8), Fraction(-1, 4)),
        (Fraction(-5, -10), Fraction(4, 8), Fraction(-1, 4)),
        (Fraction(-3, 1), Fraction(-10, 7), Fraction(30, 7)),
        (Fraction(3, -1), Fraction(10, -7), Fraction(30, 7)),
        (Fraction(-3, -1), Fraction(-10, -7), Fraction(30, 7)),
    ),
)
def test_fraction_mul(f1: Fraction, f2: Fraction, result: Fraction):
    assert f1 * f2 == result


def test_fraction_div():
    f1 = Fraction(2, 3)
    f2 = Fraction(1, 4)
    assert f1 / f2 == Fraction(8, 3)


def test_fraction_sub():
    f1 = Fraction(4, 4)
    f2 = Fraction(2, 4)
    assert f1 - f2 == Fraction(2, 4)


@pytest.mark.parametrize(
    ("f1", "f2"),
    (
        (Fraction(3, 4), Fraction(1, 5)),
        (Fraction(5, 9), Fraction(1, 5)),
        (Fraction(10, 10), Fraction(1, 5)),
    ),
)
def test_fraction_gt(f1: Fraction, f2: Fraction):
    assert f1 > f2


@pytest.mark.parametrize(
    ("f1", "f2"),
    (
        (Fraction(3, 4), Fraction(1, 5)),
        (Fraction(2, 2), Fraction(3, 3)),
        (Fraction(5, 9), Fraction(1, 5)),
        (Fraction(9), Fraction(9)),
    ),
)
def test_fraction_ge(f1: Fraction, f2: Fraction):
    assert f1 >= f2


@pytest.mark.parametrize(
    ("f1", "f2"),
    (
        (Fraction(1, 10), Fraction(1, 5)),
        (Fraction(2, 2), Fraction(9, 3)),
        (Fraction(1, 9), Fraction(1, 5)),
    ),
)
def test_fraction_lt(f1: Fraction, f2: Fraction):
    assert f1 < f2


@pytest.mark.parametrize(
    ("f1", "f2"),
    (
        (Fraction(1, 10), Fraction(1, 5)),
        (Fraction(2, 2), Fraction(9, 3)),
        (Fraction(1, 9), Fraction(1, 5)),
        (Fraction(9, 9), Fraction(9, 9)),
    ),
)
def test_fraction_lte(f1: Fraction, f2: Fraction):
    assert f1 <= f2


def test_fraction_ne():
    f1 = Fraction(2, 2)
    f2 = Fraction(9, 3)
    assert f1 != f2


def test_fraction_get_num():
    f = Fraction(3, 5)
    assert f.get_num() == 3


def test_fraction_get_den():
    f = Fraction(3, 5)
    assert f.get_den() == 5


def test_fraction_accepts_non_integers():
    with pytest.raises(Exception) as e:
        Fraction("4", "5")
    assert str(e.value) == "Non integer values passed as arguments"
