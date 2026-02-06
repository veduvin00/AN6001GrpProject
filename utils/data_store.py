import json
import os

DATA_PATH = "data/users.json"

def load_data():
    """Loads the raw dictionary of all users."""
    if not os.path.exists(DATA_PATH):
        return {}
    with open(DATA_PATH, "r") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return {}

def save_data(data):
    """Saves the dictionary of all users."""
    with open(DATA_PATH, "w") as f:
        json.dump(data, f, indent=2)

def load_user(username=None):
    """
    Loads a specific user by username.
    If no username is provided, it tries to return the first user it finds
    (This keeps your old code partially working if you forget to pass a username).
    """
    data = load_data()
    
    if username:
        return data.get(username)
    
    # Fallback for legacy calls: return the first user found
    if data:
        return list(data.values())[0]
    return None

def save_user(user_data):
    """Updates a single user inside the main dictionary."""
    data = load_data()
    username = user_data["username"]
    data[username] = user_data
    save_data(data)