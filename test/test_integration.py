import requests

def test_access_with_token():
    # login
    r = requests.post(
        "http://127.0.0.1:8000/token",
        data={"username": "admin", "password": "admin"}
    )
    token = r.json()["access_token"]

    # kald microservice
    r2 = requests.get(
        "http://127.0.0.1:8001/secret",
        headers={"Authorization": f"Bearer {token}"}
    )

    assert r2.status_code == 200