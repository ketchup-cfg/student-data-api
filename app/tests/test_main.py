from fastapi.testclient import TestClient

from app.main import app
from app.settings import settings

client = TestClient(app)


def test_get_students_returns_list_of_students():
    response = client.get(f"{settings.API_V1_STR}/students")
    assert response.status_code == 200
    assert response.json() == [
        {"name": "Trevor Pierce"},
        {"name": "Not Trevor Pierce"},
    ]
