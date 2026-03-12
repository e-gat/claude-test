from fastapi.testclient import TestClient

from app import app

client = TestClient(app)


def test_root_returns_200():
    response = client.get("/")
    assert response.status_code == 200


def test_root_returns_html():
    response = client.get("/")
    assert "text/html" in response.headers["content-type"]


def test_root_contains_hello_universe():
    response = client.get("/")
    assert "<h1>Hello Universe</h1>" in response.text


def test_root_is_valid_html():
    response = client.get("/")
    assert "<!DOCTYPE html>" in response.text
    assert "<html>" in response.text
    assert "</html>" in response.text
