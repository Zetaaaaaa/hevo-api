import requests
from loader import load_config

# Load configuration from loader.py
username, password, BASE_URL = load_config()
AUTH = (username, password)

def get_all_users():
    url = f"{BASE_URL}/accounts/users"
    headers = {"accept": "application/json"}

    try:
        response = requests.get(url, headers=headers, auth=AUTH)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Failed to get all users: {e}")
        return None

def invite_user(email):
    url = f"{BASE_URL}/accounts/users"
    headers = {
        "accept": "application/json",
        "Content-Type": "application/json"
    }
    data = {"email": email}

    try:
        response = requests.post(url, json=data, headers=headers, auth=AUTH)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Failed to invite user {email}: {e}")
        return None

def invite_user_with_roles(email, roles):
    url = f"{BASE_URL}/accounts/users-with-roles"
    headers = {
        "accept": "application/json",
        "Content-Type": "application/json"
    }
    data = {
        "email": email,
        "roles": roles
    }

    try:
        response = requests.post(url, json=data, headers=headers, auth=AUTH)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Failed to invite user {email} with roles {roles}: {e}")
        return None

def update_user_role(email, role):
    url = f"{BASE_URL}/accounts/users/{email}"
    headers = {
        "accept": "application/json",
        "Content-Type": "application/json"
    }
    data = {"role": role}

    try:
        response = requests.post(url, json=data, headers=headers, auth=AUTH)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Failed to update role for user {email}: {e}")
        return None

def delete_user(email):
    url = f"{BASE_URL}/accounts/users/{email}"
    headers = {"accept": "application/json"}

    try:
        response = requests.delete(url, headers=headers, auth=AUTH)
        response.raise_for_status()
        return response.status_code
    except requests.exceptions.RequestException as e:
        print(f"Failed to delete user {email}: {e}")
        return None

def update_user_roles(email, roles):
    url = f"{BASE_URL}/accounts/users/{email}/roles"
    headers = {
        "accept": "application/json",
        "Content-Type": "application/json"
    }
    data = {"roles": roles}

    try:
        response = requests.put(url, json=data, headers=headers, auth=AUTH)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Failed to update roles for user {email}: {e}")
        return None
