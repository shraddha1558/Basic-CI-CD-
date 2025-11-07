from app.calculator import add, subtract


def test_add():
    assert add(8, 8) == 16


def test_subtract():
    assert subtract(7, 1) == 6
