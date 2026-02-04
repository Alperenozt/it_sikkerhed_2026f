import pytest

def test_pass():
    assert True

def test_fail():
    # Fejler pga. stavefejl
    assert "Python" == "pyhton"

def test_skip():
    pytest.skip("Denne test springes over med vilje")

def test_crash():
    value = None
    value.upper()  # AttributeError

def test_fail_list_length():
    data = [1, 2, 3]
    assert len(data) == 5

def test_crash_keyerror():
    user = {"navn": "Alperen"}
    user["alder"]  # KeyError

def test_fail_math():
    assert 10 / 2 == 3

