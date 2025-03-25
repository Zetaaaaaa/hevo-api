import requests
from loader import load_config

username, password, BASE_URL = load_config()
AUTH = (username, password)

def get_all_pipeline_objects(id, search_text=None, statuses=None, category=None, starting_after=None, limit=None):
    url = f"{BASE_URL}/pipelines/{id}/objects"
    params = {}
    if search_text:
        params["search_text"] = search_text
    if statuses:
        params["statuses"] = statuses
    if category:
        params["category"] = category
    if starting_after:
        params["starting_after"] = starting_after
    if limit:
        params["limit"] = limit

    response = requests.get(url, params=params, auth=AUTH)
    return response.json()

def get_pipeline_object(id, object_name):
    url = f"{BASE_URL}/pipelines/{id}/objects/{object_name}"
    response = requests.get(url, auth=AUTH)
    return response.json()

def pause_pipeline_object(id, object_name):
    url = f"{BASE_URL}/pipelines/{id}/objects/{object_name}/pause"
    response = requests.post(url, auth=AUTH)
    return response.status_code

def resume_pipeline_object(id, object_name):
    url = f"{BASE_URL}/pipelines/{id}/objects/{object_name}/resume"
    response = requests.post(url, auth=AUTH)
    return response.status_code

def skip_pipeline_object(id, object_name):
    url = f"{BASE_URL}/pipelines/{id}/objects/{object_name}/skip"
    response = requests.post(url, auth=AUTH)
    return response.status_code

def include_pipeline_object(id, object_name):
    url = f"{BASE_URL}/pipelines/{id}/objects/{object_name}/include"
    response = requests.post(url, auth=AUTH)
    return response.status_code

def restart_pipeline_object(id, object_name):
    url = f"{BASE_URL}/pipelines/{id}/objects/{object_name}/restart"
    response = requests.post(url, auth=AUTH)
    return response.status_code

def get_object_position(id, object_name):
    url = f"{BASE_URL}/pipelines/{id}/objects/{object_name}/position"
    response = requests.get(url, auth=AUTH)
    return response.json()

def update_pipeline_object_position(id, object_name, time, month, year, key_values):
    url = f"{BASE_URL}/pipelines/{id}/objects/{object_name}/position"
    data = {
        "time": time,
        "month": month,
        "year": year,
        "key_values": key_values
    }
    response = requests.put(url, json=data, auth=AUTH)
    return response.status_code

def get_object_query_mode(id, object_name):
    url = f"{BASE_URL}/pipelines/{id}/objects/{object_name}/query-mode"
    response = requests.get(url, auth=AUTH)
    return response.json()


def update_pipeline_object_query_mode():
    id = input("Enter pipeline ID: ")
    object_name = input("Enter object name: ")

    if not id or not object_name:
        print("Pipeline ID and object name are required.")
        return


    modes = [
        "unique_incrementing", "salesforce", "full load", "xmin",
        "timestamp+incrementing", "change_tracking", "incrementing", "timestamp"
    ]

    print("\nAvailable modes:")
    for index, mode in enumerate(modes, start=1):
        print(f"{index}. {mode}")

    mode_choice = input("\nSelect a mode by number: ")
    try:
        mode = modes[int(mode_choice) - 1]
    except (IndexError, ValueError):
        print("Invalid mode selection.")
        return
    

    mode_fields = {
        "unique_incrementing": ["mode", "unique_column_name"],
        "salesforce": ["use_bulk_api"],
        "full load": ["mode"],
        "xmin": ["mode"],
        "timestamp+incrementing": ["mode", "incrementing_column_name", "timestamp_column_name"],
        "change_tracking": ["mode", "historical_enabled", "unique_column_name"],
        "incrementing": ["mode", "incrementing_column_name", "stop_on_gap"],
        "timestamp": ["mode", "timestamp_column_name", "timestamp_delay_interval_ms"]
    }


    body = {"config": {}}
    for field in mode_fields[mode]:
        value = input(f"Enter value for required '{field}': ")
        

        if value.lower() in ["true", "false"]:
            body["config"][field] = value.lower() == "true"
        elif value.isdigit():
            body["config"][field] = int(value)
        else:
            body["config"][field] = value


    url = f"{BASE_URL}/pipelines/{id}/objects/{object_name}/query-mode"
    
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json"
    }


    try:
        print("\nUpdating pipeline object query mode...")
        response = requests.put(url, json=body, headers=headers, auth=AUTH)
        response.raise_for_status()
        print("\n Successfully updated pipeline object query mode!")
        print(response.json())
    except requests.exceptions.RequestException as e:
        print(f"\n Failed to update pipeline object query mode: {e}")
