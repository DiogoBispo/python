import json
from app import create_app, db
from app.models import User
from werkzeug.security import generate_password_hash

def setup_module(module):
    app = create_app()
    app.app_context().push()
    db.drop_all()
    db.create_all()

    user = User(email="test@test.com",
                password_hash=generate_password_hash("123456"))
    db.session.add(user)
    db.session.commit()

def test_login_success():
    app = create_app()
    client = app.test_client()

    response = client.post("/auth/login",
        json={"email": "test@test.com", "password": "123456"}
    )

    assert response.status_code == 200
    assert "token" in json.loads(response.data)
