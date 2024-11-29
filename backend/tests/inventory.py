from fixtures.client import client  # noqa: F401
from fastapi import status

def test_inventory_list(client):  # noqa: F811
    response = client.get("/inventory/list")
    assert response.status_code == status.HTTP_200_OK
    assert response.json()

def test_inventory_list_post(client):  # noqa: F811
    response = client.post("/inventory/list")
    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY

def test_inventory_list_pust(client):  # noqa: F811
    response = client.put("/inventory/list")
    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY

def test_inventory_list_with_pagination(client):  # noqa: F811
    response = client.get("/inventory/list?page=2&page_size=7")
    assert response.status_code == status.HTTP_200_OK
    assert response.json()

def test_inventory_list_with_invalid_page(client):  # noqa: F811
    response = client.get("/inventory/list?page=-1&page_size=7")
    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert response.json()

def test_inventory_list_with_invalid_page_size(client):  # noqa: F811
    response = client.get("/inventory/list?page=1&page_size=-1")
    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert response.json()