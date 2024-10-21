# tests/test_main.py
from src.main import JSONPlaceholderClient, fetch_and_print_data
from typing import List, Dict
import requests
import pytest
import requests_mock
from unittest.mock import patch

# Fixture to initialize the client
@pytest.fixture
def client() -> JSONPlaceholderClient:
    return JSONPlaceholderClient()

def test_get_posts_success(client: JSONPlaceholderClient, requests_mock: requests_mock.Mocker) -> None:
    '''Test successful API response for get_posts method'''	
    mock_posts = [{"userId": 1, "id": 1, "title": "Test Post", "body": "This is a test post"}]
    requests_mock.get(f"{client.base_url}/posts", json=mock_posts, status_code=200)
    
    posts = client.get_posts()
    assert posts == mock_posts

def test_get_posts_failure(client: JSONPlaceholderClient, requests_mock: requests_mock.Mocker) -> None:
    '''Test failure in API response for get_posts method'''	
    requests_mock.get(f"{client.base_url}/posts", status_code=500)
    
    with pytest.raises(requests.exceptions.HTTPError):
        client.get_posts()

@pytest.mark.parametrize("endpoint, method, expected", [
    ("/posts", "get_posts", [{"userId": 1, "id": 1, "title": "Test Post"}]),
    ("/users", "get_users", [{"id": 1, "name": "Test User"}]),
])
def test_api_methods_success(client: JSONPlaceholderClient, requests_mock: requests_mock.Mocker, endpoint: str, method: str, expected: List[Dict]) -> None:
    '''Test successful API response for get_posts and get_users methods'''
    requests_mock.get(f"{client.base_url}{endpoint}", json=expected, status_code=200)
    
    api_method = getattr(client, method)
    result = api_method()
    assert result == expected

def test_get_posts_empty_response(client: JSONPlaceholderClient, requests_mock: requests_mock.Mocker) -> None:
    '''Test empty response for get_posts method'''	
    requests_mock.get(f"{client.base_url}/posts", json=[], status_code=200)
    
    posts = client.get_posts()
    assert posts == []

def test_get_posts_connection_error(client: JSONPlaceholderClient, requests_mock: requests_mock.Mocker) -> None:
    '''Test connection error for get_posts method'''	
    requests_mock.get(f"{client.base_url}/posts", exc=requests.exceptions.ConnectionError)
    
    with pytest.raises(requests.exceptions.ConnectionError):
        client.get_posts()

@pytest.mark.parametrize("endpoint, method, status_code", [
    ("/posts", "get_posts", 400),
    ("/users", "get_users", 404),
])
def test_api_methods_failure(client: JSONPlaceholderClient, requests_mock: requests_mock.Mocker, endpoint: str, method: str, status_code: int) -> None:
    '''Test failure in API response for get_posts and get_users methods'''
    requests_mock.get(f"{client.base_url}{endpoint}", status_code=status_code)
    
    api_method = getattr(client, method)
    with pytest.raises(requests.exceptions.HTTPError):
        api_method()

@patch('logging.info')
@patch.object(JSONPlaceholderClient, 'get_posts')
@patch.object(JSONPlaceholderClient, 'get_users')
def test_fetch_and_print_data(mock_get_users, mock_get_posts, mock_logging_info):
    mock_get_posts.return_value = [{"userId": 1, "id": 1, "title": "Test Post"}]
    mock_get_users.return_value = [{"id": 1, "name": "Test User"}]

    client = JSONPlaceholderClient()
    fetch_and_print_data(client)

    # Check that logging.info was called with the correct arguments
    mock_logging_info.assert_any_call(f"Posts: {mock_get_posts.return_value}")
    mock_logging_info.assert_any_call(f"Users: {mock_get_users.return_value}")
