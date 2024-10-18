# src/main.py
import requests
from typing import List, Dict, Any

class JSONPlaceholderClient:
    def __init__(self, base_url: str = "https://jsonplaceholder.typicode.com") -> None:
        self.base_url: str = base_url

    def get_posts(self) -> List[Dict[str, Any]]:
        '''Fetches posts from the JSONPlaceholder API
        Returns:
            List[Dict[str, Any]]: List of posts
        '''
        response: requests.Response = requests.get(f"{self.base_url}/posts")
        response.raise_for_status()
        posts: List[Dict[str, Any]] = response.json()
        return posts

    def get_users(self) -> List[Dict[str, Any]]:
        '''Fetches users from the JSONPlaceholder API
        Returns:
            List[Dict[str, Any]]: List of users
        '''
        response: requests.Response = requests.get(f"{self.base_url}/users")
        response.raise_for_status()
        users: List[Dict[str, Any]] = response.json()
        return users

def fetch_and_print_data(client: JSONPlaceholderClient) -> None:
    '''Fetches and prints posts and users from the JSONPlaceholder API'''
    posts: List[Dict[str, Any]] = client.get_posts()
    users: List[Dict[str, Any]] = client.get_users()

    print("Posts:", posts)
    print("Users:", users)

def main() -> None:
    client: JSONPlaceholderClient = JSONPlaceholderClient()
    fetch_and_print_data(client)

if __name__ == "__main__":
    main()
