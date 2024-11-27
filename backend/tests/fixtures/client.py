import pytest
from fastapi.testclient import TestClient
from src.main import app  # Import FastAPI app from the src.main module

@pytest.fixture(scope="session")
def client():
    """
    Fixture to create a TestClient for FastAPI app.
    Scope set to "session" so the client is shared across all tests.
    """
    client = TestClient(app)
    yield client
