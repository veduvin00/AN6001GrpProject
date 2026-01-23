import pandas as pd

USERS_CSV = "data/users.csv"

def validate_user(username, password):
    users = pd.read_csv(USERS_CSV)
    match = users[
        (users["username"] == username) &
        (users["password"] == password)
    ]
    return not match.empty
