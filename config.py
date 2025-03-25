# config.py
import json

CONFIG_FILE = "config.json"

DOMAIN_MAP = {
    'us': 'https://us.hevodata.com/api/public/v2.0',
    'us2': 'https://us2.hevodata.com/api/public/v2.0',
    'in': 'https://in.hevodata.com/api/public/v2.0',
    'asia': 'https://asia.hevodata.com/api/public/v2.0',
    'eu': 'https://eu.hevodata.com/api/public/v2.0',
    'au': 'https://au.hevodata.com/api/public/v2.0'
}

def set_config():
    username = input("Enter username: ")
    password = input("Enter password: ")
    domain = input("Enter domain (us, us2, in, asia, eu, au): ")

    if domain in DOMAIN_MAP:
        base_url = DOMAIN_MAP[domain]
        config = {
            "username": username,
            "password": password,
            "base_url": base_url
        }

        with open(CONFIG_FILE, "w") as f:
            json.dump(config, f, indent=4)

        print(f"Configuration set! Base URL: {base_url}")
        print("Configuration saved successfully!")
    else:
        raise ValueError(f"Invalid domain: {domain}")

if __name__ == "__main__":
    set_config()
