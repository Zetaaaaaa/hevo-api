import requests
from loader import load_config

# Load configuration from loader.py
username, password, BASE_URL = load_config()
AUTH = (username, password)

def get_all_workflows():
    url = f"{BASE_URL}/workflows"
    headers = {"accept": "application/json"}

    try:
        response = requests.get(url, headers=headers, auth=AUTH)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Failed to get all workflows: {e}")
        return None

def run_workflow(id):
    url = f"{BASE_URL}/workflows/{id}/run-now"
    headers = {"accept": "application/json"}

    try:
        response = requests.post(url, headers=headers, auth=AUTH)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Failed to run workflow with ID {id}: {e}")
        return None

def get_workflow(id):
    url = f"{BASE_URL}/workflows/{id}"
    headers = {"accept": "application/json"}

    try:
        response = requests.get(url, headers=headers, auth=AUTH)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Failed to get workflow with ID {id}: {e}")
        return None
