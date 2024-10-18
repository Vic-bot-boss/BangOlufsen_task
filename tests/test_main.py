# tests/test_main.py
from src.main import JSONPlaceholderClient
from typing import List, Dict
import requests
import pytest
import requests_mock

@pytest.fixture
def client() -> JSONPlaceholderClient:
    return JSONPlaceholderClient()

def test_get_posts_success(client: JSONPlaceholderClient, requests_mock: requests_mock.Mocker) -> None:
    # Mock the API response
    mock_posts: List[Dict] = [{"userId": 1, "id": 1, "title": "Test Post", "body": "This is a test post"}]
    requests_mock.get(f"{client.base_url}/posts", json=mock_posts, status_code=200)
    
    posts = client.get_posts()
    assert posts == mock_posts

def test_get_posts_failure(client: JSONPlaceholderClient, requests_mock: requests_mock.Mocker) -> None:
    # Mock the API to return a 500 error
    requests_mock.get(f"{client.base_url}/posts", status_code=500)
    
    with pytest.raises(requests.exceptions.HTTPError):
        client.get_posts()


@pytest.mark.parametrize("endpoint, method", [
    ("/posts", "get_posts"),
    ("/users", "get_users"),
])
def test_api_methods_success(client: JSONPlaceholderClient, requests_mock: requests_mock.Mocker, endpoint: str, method: str) -> None:
    mock_data = [{"id": 1, "name": "Test"}]
    requests_mock.get(f"{client.base_url}{endpoint}", json=mock_data, status_code=200)
    
    api_method = getattr(client, method)
    result = api_method()
    assert result == mock_data


@pytest.mark.api
def test_get_users_success(client: JSONPlaceholderClient, requests_mock: requests_mock.Mocker) -> None:
    # Mock response
    mock_users = [{"id": 1, "name": "Test User"}]
    requests_mock.get(f"{client.base_url}/users", json=mock_users, status_code=200)
    
    users = client.get_users()
    assert users == mock_users
