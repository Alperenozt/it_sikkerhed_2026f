def validate_password(password):
    return len(password) >= 8


def test_password_graensevaerdi():
    assert validate_password("1234567") is False  # 7 tegn
    assert validate_password("12345678") is True  # 8 tegn
    assert validate_password("123456789") is True # 9 tegn
