# tests/conftest.py
import pytest
from main import app  # Предположим, что у вас есть функция создания приложения
from fastapi.testclient import TestClient
from unittest.mock import patch

@pytest.fixture
def client():
    with TestClient(app) as c:
        yield c

@pytest.fixture
def mock_external_api():
    with patch('app.services.external_api.fetch_coordinates') as mock:
        yield mock

