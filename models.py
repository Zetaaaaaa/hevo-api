import requests
from loader import load_config

username, password, BASE_URL = load_config()
AUTH = (username, password)

def get_model(id):
    url = f"{BASE_URL}/models/{id}"
    response = requests.get(url, auth=AUTH)
    return response.json()

def update_model(id, name, source_query, destination_table_details, load_type):
    url = f"{BASE_URL}/models/{id}"
    payload = {
        "name": name,
        "source_query": source_query,
        "destination_table_details": destination_table_details,  # Should be a dict or list based on the API spec
        "load_type": load_type
    }
    response = requests.put(url, json=payload, auth=AUTH)
    return response.status_code

def get_all_models():
    url = f"{BASE_URL}/models"
    response = requests.get(url, auth=AUTH)
    return response.json()

def create_model(name, source_destination_id, destination_table_objects, source_query=None, schedule=None):
    url = f"{BASE_URL}/models"
    headers = {
        "accept": "application/json",
        "Content-Type": "application/json"
    }
    data = {
        "name": name,
        "source_destination_id": source_destination_id,
        "destination_table_objects": destination_table_objects
    }
    if source_query is not None:
        data["source_query"] = source_query
    if schedule is not None:
        data["schedule"] = schedule

    try:
        response = requests.post(url, json=data, headers=headers, auth=AUTH)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Failed to create model: {e}")
        return None


def update_model_activity_schedule(id, state):
    url = f"{BASE_URL}/models/{id}/status"
    payload = {"state": state}
    response = requests.put(url, json=payload, auth=AUTH)
    return response.status_code

def run_model(id):
    url = f"{BASE_URL}/models/{id}/run-now"
    response = requests.post(url, auth=AUTH)
    return response.status_code

def update_model_schedule(id, schedule_type, frequency, cron_expression, destination_tables):
    url = f"{BASE_URL}/models/{id}/schedule"
    payload = {
        "type": schedule_type,
        "frequency": frequency,
        "cron_expression": cron_expression,
        "destination_tables": destination_tables  # Should be a list based on the API spec
    }
    response = requests.put(url, json=payload, auth=AUTH)
    return response.status_code

def reset_model(id):
    url = f"{BASE_URL}/models/{id}/reset"
    response = requests.delete(url, auth=AUTH)
    return response.status_code
