users = {
    "admin": "admin123"
}

def validate_user(username, password):
    return users.get(username) == password
