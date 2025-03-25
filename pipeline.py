import requests
from loader import load_config

username, password, BASE_URL = load_config()
AUTH = (username, password)

def get_pipeline(id):
    url = f"{BASE_URL}/pipelines/{id}"
    response = requests.get(url, auth=AUTH)
    return response.json()

def delete_pipeline(id):
    url = f"{BASE_URL}/pipelines/{id}"
    response = requests.delete(url, auth=AUTH)
    return response.status_code

def get_pipeline_object_stats(id, object_name):
    url = f"{BASE_URL}/pipelines/{id}/objects/{object_name}/stats"
    response = requests.get(url, auth=AUTH)
    return response.json()

def get_pipelines(limit=None, starting_after=None):
    url = f"{BASE_URL}/pipelines"
    params = {}
    if limit:
        params["limit"] = limit
    if starting_after:
        params["starting_after"] = starting_after
    response = requests.get(url, params=params, auth=AUTH)
    return response.json()

def update_pipeline_activity_status(id, state):
    url = f"{BASE_URL}/pipelines/{id}/status"
    data = {"state": state}
    
    try:
        response = requests.put(url, json=data, auth=AUTH)
        response.raise_for_status()
        return response.status_code
    except requests.exceptions.RequestException as e:
        print(f"Failed to update activity status for pipeline with ID {id}: {e}")
        return None


def run_pipeline(id):
    url = f"{BASE_URL}/pipelines/{id}/run-now"
    response = requests.post(url, auth=AUTH)
    return response.status_code

def get_pipeline_position(id):
    url = f"{BASE_URL}/pipelines/{id}"
    response = requests.get(url, auth=AUTH)
    return response.json()

def update_log_based_pipeline_position(id, file_name, offset):
    url = f"{BASE_URL}/pipelines/{id}/position"
    data = {"file_name": file_name, "offset": offset}
    response = requests.put(url, json=data, auth=AUTH)
    return response.status_code

def update_pipeline_priority(id, priority):
    url = f"{BASE_URL}/pipelines/{id}/priority"
    data = {"priority": priority}
    response = requests.put(url, json=data, auth=AUTH)
    return response.status_code

def get_pipeline_schedule(id):
    url = f"{BASE_URL}/pipelines/{id}/schedule"
    response = requests.get(url, auth=AUTH)
    return response.json()

def update_pipeline_schedule(id, frequency):
    url = f"{BASE_URL}/pipelines/{id}/schedule"
    data = {"frequency": frequency}
    response = requests.put(url, json=data, auth=AUTH)
    return response.status_code


def update_destination_configuration():
    destination_types = {
        "BIGQUERY": [
            "bucket", "populate_loaded_timestamp", "oauth_account_id", 
            "project_id", "enable_streaming_inserts", "dataset_name", 
            "service_account_id"
        ],
        "SNOWFLAKE": [
            "populate_loaded_timestamp", "db_name", "account_name", 
            "db_user", "schema_name", "region", "warehouse", "db_password"
        ],
        "POSTGRES": [
            "ssh_port", "db_name", "use_ssl", "db_user", "ssh_host", 
            "schema_name", "db_port", "db_host", "db_password", "ssh_user"
        ],
        "MYSQL": [
            "ssh_port", "db_name", "db_user", "ssh_host", "schema_name", 
            "db_port", "db_host", "db_password", "ssh_user"
        ],
        "DATABRICKS": [
            "vacuum_delta_tables", "populate_loaded_timestamp", "port", 
            "optimize_delta_tables", "http_path", "schema_name", 
            "server_hostname", "personal_access_token", "external_location"
        ],
        "REDSHIFT": [
            "populate_loaded_timestamp", "ssh_port", "db_name", "db_user", 
            "ssh_host", "schema_name", "db_port", "db_host", "db_password", 
            "ssh_user"
        ],
        "MS_SQL": [
            "ssh_port", "db_name", "db_user", "ssh_host", "schema_name", 
            "db_port", "db_host", "db_password", "ssh_user"
        ],
        "AZURE_SYNAPSE": [
            "populate_loaded_timestamp", "ssh_port", "db_name", "db_user", 
            "ssh_host", "schema_name", "db_port", "db_host", "db_password", 
            "ssh_user"
        ],
        "AURORA": [
            "ssh_port", "db_name", "db_user", "ssh_host", "schema_name", 
            "db_port", "db_host", "db_password", "ssh_user"
        ]
    }
    
    id = input("Enter value for required 'id': ")
    type = input("Enter value for required 'type': ").upper()

    if type not in destination_types:
        print(f"Invalid type: {type}")
        return
    
    kwargs = {}
    
    for field in destination_types[type]:
        value = input(f"Enter value for required '{field}': ")
        
        if value.lower() in ["true", "false"]:
            kwargs[field] = value.lower() == "true"
        elif value.isdigit():
            kwargs[field] = int(value)
        else:
            kwargs[field] = value
    
    print("\nUpdating destination with the following values:")
    print(f"ID: {id}")
    print(f"Type: {type}")
    print(f"Kwargs: {kwargs}")
    
    url = f"{BASE_URL}/destinations/{id}"
    data = {
        "type": type,
        **kwargs
    }

    response = requests.put(url, json=data, auth=AUTH)

    if response.status_code == 200:
        print("Destination updated successfully!")
    else:
        print(f"Failed to update destination: {response.status_code} - {response.text}")