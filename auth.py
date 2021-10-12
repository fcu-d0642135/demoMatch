from data import members


def login(username, password):
    for i in members:
        if members[i]['username'] == username and members[i]['password'] == password:
            return True
    return False


def identify(username):
    for i in members:
        if members[i]['username'] == username:
            return members[i]['identify']

