from data import members


def login(username, password):
    for i in members:
        if members[i]['username'] == username and members[i]['password'] == password:
            return True
    return False


if __name__ == '__main__':
    print("請登入 ...")
    username = input("UserName:")
    password = input("Password:")
    login = login(username, password)
    if login:
        print("登入成功")
    else:
        print("登入失敗")
