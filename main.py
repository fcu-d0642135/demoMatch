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


def supplyChoice():
    pass


def demandChoice():
    pass


if __name__ == '__main__':
    print("請登入 ...")
    username = input("UserName:")
    password = input("Password:")
    login = login(username, password)
    if login:
        print("登入成功")
        identify = identify(username)
        if identify == 'supply':
            supplyChoice()
        elif identify == 'demand':
            demandChoice()
    else:
        print("登入失敗")
