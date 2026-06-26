import pytest
from src.test_strategier.login_system import LoginSystem


@pytest.mark.parametrize("korrekt_kode, laast, forventet", [
    (True, False, "ok"),
    (False, False, "forkert"),
    (False, True, "låst"),
    (True, True, "låst"),
])
def test_login_decision_table(korrekt_kode, laast, forventet):
    system = LoginSystem()
    system.create_user("test", "kode1234")

    if laast:
        system.locked_users.add("test")

    password = "kode1234" if korrekt_kode else "forkert"
    assert system.login("test", password) == forventet
