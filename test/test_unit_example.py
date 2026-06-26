import pytest
from src.test_strategier.login_system import LoginSystem

def test_unit_login_ok():
    system = LoginSystem()
    system.create_user("unit", "test1234")
    assert system.login("unit", "test1234") == "ok" 
