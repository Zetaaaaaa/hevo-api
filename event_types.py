import requests
from loader import load_config

username, password, BASE_URL = load_config()
AUTH = (username, password)

def get_event_types(id, search_text=None, starting_after=None, limit=None):
    url = f"{BASE_URL}/pipelines/{id}/event-types"
    params = {}
    if search_text:
        params["search_text"] = search_text
    if starting_after:
        params["starting_after"] = starting_after
    if limit:
        params["limit"] = limit
    
    response = requests.get(url, params=params, auth=AUTH)
    return response.json()

def skip_event_type(id, event_type):
    url = f"{BASE_URL}/pipelines/{id}/event-types/{event_type}/skip"
    response = requests.put(url, auth=AUTH)
    return response.status_code

def include_event_type(id, event_type):
    url = f"{BASE_URL}/pipelines/{id}/event-types/{event_type}/include"
    response = requests.put(url, auth=AUTH)
    return response.status_code
