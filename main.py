from auth import login, identify
from supply import supplyChoice
from demand import demandChoice


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
