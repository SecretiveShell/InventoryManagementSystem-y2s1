import pytest
import httpx


@pytest.fixture
def client():
    """
    Fixture to create a TestClient for FastAPI app.
    Scope set to "session" so the client is shared across all tests.
    """
    client = httpx.Client(base_url="http://localhost:8000")
    yield client
