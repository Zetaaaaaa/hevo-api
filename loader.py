# loader.py
import json
import os

CONFIG_FILE_PATH = "config.json"

def load_config():
    if os.path.exists(CONFIG_FILE_PATH):
        with open(CONFIG_FILE_PATH, "r") as f:
            config = json.load(f)
            return config["username"], config["password"], config["base_url"]
    else:
        raise ValueError("Configuration is missing. Please run config.py first.")
