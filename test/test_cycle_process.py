from src.test_strategier.login_system import LoginSystem

def test_bruger_livscyklus():
    system = LoginSystem()
    system.create_user("bob", "hemmelig123")

    # Korrekt login
    assert system.login("bob", "hemmelig123") == "ok"

    # Forkerte forsøg
    assert system.login("bob", "forkert") == "forkert"
    assert system.login("bob", "forkert") == "forkert"
    assert system.login("bob", "forkert") == "forkert"

    # Konto er nu låst
    assert system.login("bob", "hemmelig123") == "låst"
