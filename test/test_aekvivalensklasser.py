import pytest

def validate_username(username):
    return 3 <= len(username) <= 20


@pytest.mark.parametrize("username, forventet", [
    ("ab", False),          # for kort
    ("abc", True),          # gyldig
    ("brugernavn123", True),
    ("a" * 21, False),      # for langt
    ("", False),            # tom
])
def test_brugernavn_aekvivalensklasser(username, forventet):
    assert validate_username(username) == forventet
