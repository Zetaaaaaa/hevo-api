import requests
from loader import load_config


username, password, BASE_URL = load_config()
AUTH = (username, password)

def update_pipeline_auto_mapping_status(id, state):
    url = f"{BASE_URL}/pipelines/{id}/auto-mapping"
    payload = {"state": state}

    try:
        response = requests.put(url, json=payload, auth=AUTH)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Failed to update pipeline auto-mapping status for ID {id}: {e}")
        return None

def get_schema_mapping(id, event_type):
    url = f"{BASE_URL}/pipelines/{id}/mappings/{event_type}"

    try:
        response = requests.get(url, auth=AUTH)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Failed to get schema mapping for ID {id}, event type {event_type}: {e}")
        return None

def update_schema_mapping(id, event_type, destination_table, field_mappings):
    url = f"{BASE_URL}/pipelines/{id}/mappings/{event_type}"
    payload = {
        "destination_table": destination_table,
        "field_mappings": field_mappings
    }

    try:
        response = requests.put(url, json=payload, auth=AUTH)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Failed to update schema mapping for ID {id}, event type {event_type}: {e}")
        return None
