from data import credentials


def login(username, password):
    attempts = 3
    while attempts > 0:
        if username in credentials and credentials[username] == password:
            return True
        attempts -= 1
    return False
