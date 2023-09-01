import pytest
from project import app


def test_index():
    response = app.test_client().get("/")
    assert b"<title> Hi, I'm Marissa Shaffer. </title>" in response.data
    assert response.status_code == 200

def test_about():
    about_response = app.test_client().get("/about")
    assert b"<title> About </title>" in about_response.data
    assert about_response.status_code == 200

def test_projects():
    projects_response = app.test_client().get("/projects")
    assert b"<title> Projects </title>" in projects_response.data
    assert projects_response.status_code == 200

def test_contact():
    contact_response = app.test_client().get("/contact")
    assert b"<title> Contact </title>" in contact_response.data
    assert contact_response.status_code == 200

    contact_post_response = app.test_client().post("/contact", data={
        "name": "Testing Contact",
        "email": "testemail@gmail.com",
        "subject": "This is just a test",
        "message": "Hi! Just testing that the form is working",
    })
    assert contact_post_response.status_code == 200