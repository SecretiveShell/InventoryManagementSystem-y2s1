from fixtures.client import client  # noqa: F401


def test_books_list(client):  # noqa: F811
    response = client.get("/books")
    assert response.status_code == 200
    assert response.json()
