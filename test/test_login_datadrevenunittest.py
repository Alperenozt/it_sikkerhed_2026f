import pytest
from src.test_strategier.login_system import LoginSystem

@pytest.mark.parametrize(
    "password, korrekt, laast, forventet",
    [
        ("1234567", False, False, "forkert"),   # for kort password (grænseværdi)
        ("12345678", True, False, "ok"),        # gyldigt password
        ("12345678", True, True, "låst"),       # korrekt password men konto låst
        ("forkertpw", False, True, "låst"),     # forkert + låst
    ]
)
def test_login_datadreven(password, korrekt, laast, forventet):
    system = LoginSystem()
    system.create_user("test", "12345678")

    if laast:
        system.locked_users.add("test")

    # Brug korrekt eller forkert password
    brugt_password = "12345678" if korrekt else password

    assert system.login("test", brugt_password) == forventet