from fastapi.testclient import TestClient

from app.main import app
from app.models.students import Student
from app.settings import settings

client = TestClient(app)


def test_get_students_returns_200_status_code():
    """Ensure that GET requests to /students return the expected status code."""
    response = client.get(f"{settings.API_V1_STR}/students")
    assert response.status_code == 200


def test_get_students_returns_students():
    """Ensure that GET requests to /students return the expected type."""
    response = client.get(f"{settings.API_V1_STR}/students")
    actual = sorted(set([list(s.keys())[0] for s in response.json()]))
    expected = sorted(Student.__fields__.keys())
    assert expected == actual
