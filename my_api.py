import requests
import json
from loader import load_config

def fetch_data():
    username, password, base_url = load_config()

    url = f"{base_url}/pipelines/6590"
    auth = (username, password)

    try:
        response = requests.get(url, auth=auth)
        response.raise_for_status()
        
        data = response.json()
        print("Data fetched:")
        print(json.dumps(data, indent=4))
    except requests.exceptions.RequestException as e:
        print(f"Error while fetching data: {e}")

if __name__ == "__main__":
    fetch_data()
