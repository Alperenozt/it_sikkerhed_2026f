import pytest

# ─────────────── Basis tests ─────────────── echo "# test" >> README.md

def test_pass():
    # Simpel matematik der passer
    assert 4 - 1 == 3


def test_fail():
    # Fejler fordi teksten ikke matcher
    assert "Python" == "pyhton"   # stavefejl med vilje


@pytest.mark.skip(reason="Denne test springes over i eksemplet")
def test_skip():
    # Bliver aldrig kørt
    assert 999 == 0


def test_crash():
    # Crasher pga. adgang til NoneType
    value = None
    value.upper()   # AttributeError → crash


# ─────────────── Ekstra tests ───────────────

def test_fail_list_length():
    # Fejler fordi længden ikke passer
    data = [1, 2, 3]
    assert len(data) == 5


def test_crash_keyerror():
    # Crasher pga. manglende nøgle i dictionary
    user = {"navn": "Alperen"}
    return user["alder"]   # KeyError


def test_fail_math():
    # Fejler på forkert beregning
    assert 10 / 2 == 3