import json
from app import create_app

def test_get_products_requires_token():
    app = create_app()
    client = app.test_client()

    response = client.get("/products")

    assert response.status_code == 401
