from auth import login, identify
from supply import supply_choice
from demand import demand_choice


if __name__ == '__main__':
    print("請登入 ...")
    username = input("UserName:")
    password = input("Password:")
    login = login(username, password)
    if login:
        print("登入成功")
        identify = identify(username)
        if identify == 'supply':
            supply_choice()
        elif identify == 'demand':
            demand_choice()
    else:
        print("登入失敗")
