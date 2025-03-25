import requests
from loader import load_config

# Load configuration from loader.py
username, password, BASE_URL = load_config()
AUTH = (username, password)

def get_transformation_code(id):
    url = f"{BASE_URL}/pipelines/{id}/transformations"
    headers = {"accept": "application/json"}

    try:
        response = requests.get(url, headers=headers, auth=AUTH)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Failed to get transformation code for ID {id}: {e}")
        return None

def update_transformation_code(id, script):
    url = f"{BASE_URL}/pipelines/{id}/transformations"
    headers = {
        "accept": "application/json",
        "Content-Type": "application/json"
    }
    data = {"script": script}

    try:
        response = requests.put(url, json=data, headers=headers, auth=AUTH)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Failed to update transformation code for ID {id}: {e}")
        return None

def test_transformation_sample(id, script, event_name, properties):
    url = f"{BASE_URL}/pipelines/{id}/transformations/test"
    headers = {
        "accept": "application/json",
        "Content-Type": "application/json"
    }
    data = {
        "script": script,
        "event_name": event_name,
        "properties": properties
    }

    try:
        response = requests.post(url, json=data, headers=headers, auth=AUTH)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Failed to test transformation sample for ID {id}: {e}")
        return None

def get_transformation_sample(id, event_name=None):
    url = f"{BASE_URL}/pipelines/{id}/transformations/sample"
    params = {}
    if event_name:
        params["event_name"] = event_name
    headers = {"accept": "application/json"}

    try:
        response = requests.get(url, params=params, headers=headers, auth=AUTH)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Failed to get transformation sample for ID {id}: {e}")
        return None
