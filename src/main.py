# src/main.py
import requests
from typing import List
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(levelname)s:%(message)s')

class JSONPlaceholderClient:
    def __init__(self, base_url: str = "https://jsonplaceholder.typicode.com") -> None:
        self.base_url: str = base_url

    def get_posts(self) -> List[dict]:
        '''Fetches posts from the JSONPlaceholder API
        Returns:
            List[dict]: List of posts
        '''
        try:
            response: requests.Response = requests.get(f"{self.base_url}/posts")
            response.raise_for_status()
            posts: List[dict] = response.json()
            return posts
        except requests.RequestException as e:
            logging.error(f"Error fetching posts: {e}")
            raise

    def get_users(self) -> List[dict]:
        '''Fetches users from the JSONPlaceholder API
        Returns:
            List[dict]: List of users
        '''
        try:
            response: requests.Response = requests.get(f"{self.base_url}/users")
            response.raise_for_status()
            users: List[dict] = response.json()
            return users
        except requests.RequestException as e:
            logging.error(f"Error fetching users: {e}")
            raise

def fetch_and_print_data(client: JSONPlaceholderClient) -> None:
    '''Fetches and prints posts and users from the JSONPlaceholder API'''
    try:
        posts: List[dict] = client.get_posts()
        users: List[dict] = client.get_users()

        logging.info(f"Posts: {posts}")
        logging.info(f"Users: {users}")
    except Exception as e:
        logging.error(f"An error occurred while fetching data: {e}")

def main() -> None:
    client: JSONPlaceholderClient = JSONPlaceholderClient()
    fetch_and_print_data(client)

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        logging.critical(f"Application terminated due to an unexpected error: {e}")
