from app.calculator import add, subtract

def test_add():
    assert add(1, 1) == 2

def test_subtract():
    assert subtract(5, 2) == 3
