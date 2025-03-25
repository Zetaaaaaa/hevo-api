import requests
from loader import load_config

username, password, BASE_URL = load_config()
AUTH = (username, password)

def get_destination(id):
    url = f"{BASE_URL}/destinations/{id}"
    response = requests.get(url, auth=AUTH)
    return response.json()

def get_destinations(starting_after=None, limit=None):
    url = f"{BASE_URL}/destinations"
    params = {}
    if starting_after:
        params["starting_after"] = starting_after
    if limit:
        params["limit"] = limit

    response = requests.get(url, params=params, auth=AUTH)
    return response.json()

def get_destination_table_stats(id, table_name, duration=None):
    url = f"{BASE_URL}/destinations/{id}/tables/{table_name}/stats"
    params = {}
    if duration:
        params["duration"] = duration
    
    response = requests.get(url, params=params, auth=AUTH)
    return response.json()

def load_events_to_destination(id):
    url = f"{BASE_URL}/destinations/{id}/load-now"
    response = requests.post(url, auth=AUTH)
    return response.status_code


# def create_destination():
#     destination_types = {
#         "BIGQUERY": [
#             "bucket", "populate_loaded_timestamp", "oauth_account_id", 
#             "project_id", "enable_streaming_inserts", "dataset_name", 
#             "service_account_id"
#         ],
#         "SNOWFLAKE": [
#             "populate_loaded_timestamp", "db_name", "account_name", 
#             "db_user", "schema_name", "region", "warehouse", "db_password"
#         ],
#         "POSTGRES": [
#             "ssh_port", "db_name", "use_ssl", "db_user", "ssh_host", 
#             "schema_name", "db_port", "db_host", "db_password", "ssh_user"
#         ],
#         "MYSQL": [
#             "ssh_port", "db_name", "db_user", "ssh_host", "schema_name", 
#             "db_port", "db_host", "db_password", "ssh_user"
#         ],
#         "DATABRICKS": [
#             "vacuum_delta_tables", "populate_loaded_timestamp", "port", 
#             "optimize_delta_tables", "http_path", "schema_name", 
#             "server_hostname", "personal_access_token", "external_location"
#         ],
#         "REDSHIFT": [
#             "populate_loaded_timestamp", "ssh_port", "db_name", "db_user", 
#             "ssh_host", "schema_name", "db_port", "db_host", "db_password", 
#             "ssh_user"
#         ],
#         "MS_SQL": [
#             "ssh_port", "db_name", "db_user", "ssh_host", "schema_name", 
#             "db_port", "db_host", "db_password", "ssh_user"
#         ],
#         "AZURE_SYNAPSE": [
#             "populate_loaded_timestamp", "ssh_port", "db_name", "db_user", 
#             "ssh_host", "schema_name", "db_port", "db_host", "db_password", 
#             "ssh_user"
#         ],
#         "AURORA": [
#             "ssh_port", "db_name", "db_user", "ssh_host", "schema_name", 
#             "db_port", "db_host", "db_password", "ssh_user"
#         ]
#     }
    
#     name = input("Enter value for required 'name': ")
#     type = input("Enter value for required 'type': ").upper()

#     if type not in destination_types:
#         print(f"Invalid type: {type}")
#         return
    
#     kwargs = {}
    
#     for field in destination_types[type]:
#         value = input(f"Enter value for required '{field}': ")
        
#         if value.lower() in ["true", "false"]:
#             kwargs[field] = value.lower() == "true"
#         elif value.isdigit():
#             kwargs[field] = int(value)
#         else:
#             kwargs[field] = value
    
#     print("\nCreating destination with the following values:")
#     print(f"Name: {name}")
#     print(f"Type: {type}")
#     print(f"Kwargs: {kwargs}")

#     url = f"{BASE_URL}/destinations"
#     data = {
#         "name": name,
#         "type": type,
#         **kwargs
#     }

#     response = requests.post(url, json=data, auth=AUTH)

#     if response.status_code == 201:
#         print("Destination created successfully!")
#     else:
#         print(f"Failed to create destination: {response.status_code} - {response.text}")
