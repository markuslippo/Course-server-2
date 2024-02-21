from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_read_course():
    response = client.get("/courses/CS-E4190")
    assert response.status_code == 200
    assert response.json() == {
        "id": "CS-E4190",
        "name": "Cloud software and systems",
        "instructor": "Mario Di francesco",
        "keyword": ["cloud", "container"],
    }


def test_read_nonexistent_course():
    response = client.get("/courses/nonexistent_course")
    assert response.status_code == 404
    assert response.json() == {"detail": "Course does not exist"}


def test_create_course():
    course_data = {
        "id": "newid",
        "name": "newname",
        "instructor": "newinstructor",
        "keyword": ["new", "course"],
    }
    response = client.post("/courses/", json=course_data)
    assert response.status_code == 200
    assert response.json() == course_data


def test_create_existing_course():
    course_data = {
        "id": "CS-E4190", 
        "name": "Cloud software and systems",
        "instructor": "Mario Di francesco",
        "keyword": ["cloud", "container"],
    }
    response = client.post("/courses/", json=course_data)
    assert response.status_code == 400
    assert response.json() == {"detail": "Course already exists"}
