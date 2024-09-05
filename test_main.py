import os
from fastapi.testclient import TestClient  # type: ignore
from dotenv import load_dotenv  # type: ignore
from main import app

load_dotenv()

client = TestClient(app)


def test_app_title_and_version():
    assert app.title == "Fund Manager"
    assert app.version == os.getenv("VERSION")


def test_home_endpoint():
    response = client.get("/")
    assert response.status_code == 404


def test_fund_router():
    response = client.get("/funds")
    assert response.status_code == 200


def test_transaction_router():
    response = client.get("/transactions")
    assert response.status_code == 200
