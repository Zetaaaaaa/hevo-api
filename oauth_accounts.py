import requests
from loader import load_config

# Load configuration from loader.py
username, password, BASE_URL = load_config()
AUTH = (username, password)

def get_oauth_accounts(provider):
    url = f"{BASE_URL}/accounts/oauth"
    params = {"provider": provider}
    headers = {"accept": "application/json"}

    try:
        response = requests.get(url, params=params, headers=headers, auth=AUTH)
        response.raise_for_status()  # Raise exception for 4xx and 5xx responses
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Failed to get OAuth accounts: {e}")
        return None

def get_oauth_account(id):
    url = f"{BASE_URL}/accounts/oauth/{id}"
    headers = {"accept": "application/json"}

    try:
        response = requests.get(url, headers=headers, auth=AUTH)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Failed to get OAuth account with ID {id}: {e}")
        return None

def remove_oauth_account(id):
    url = f"{BASE_URL}/accounts/oauth/{id}"
    headers = {"accept": "application/json"}

    try:
        response = requests.delete(url, headers=headers, auth=AUTH)
        response.raise_for_status()
        return response.status_code
    except requests.exceptions.RequestException as e:
        print(f"Failed to remove OAuth account with ID {id}: {e}")
        return None
