import pytest

def test_pass():
    assert True

def test_fail():
    assert "Python" == "Python"

def test_skip():
    pytest.skip("Denne test springes over med vilje")

def test_crash():
    value = "python"
    assert value.upper() == "PYTHON"

def test_fail_list_length():
    data = [1, 2, 3]
    assert len(data) == 3

def test_crash_keyerror():
    user = {"navn": "Alperen", "alder": 18}
    assert user["alder"] == 18

def test_fail_math():
    assert 10 / 2 == 5


