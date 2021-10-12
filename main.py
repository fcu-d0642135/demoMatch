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
    choices = {
        '0': {
            'name': '設定媒合需求',
            'func': setMatchRequirements,
        },
        '1': {
            'name': '查詢媒合結果',
            'func': selectMatchResult,
        }
    }
    
    for i in choices:
        print(f'{i}: {choices[i]["name"]}')
    choice = input('請選擇 ...')
    choices[choice]['func']()


def demandChoice():
    choices = {
        '0': {
            'name': '設定求職需求',
            'func': setJobHunting,
        },
        '1': {
            'name': '查詢求職結果',
            'func': selectJobHunting,
        }
    }

    for i in choices:
        print(f'{i}: {choices[i]["name"]}')
    choice = input('請選擇 ...')
    choices[choice]['func']()


def setMatchRequirements():
    pass


def selectMatchResult():
    pass


def setJobHunting():
    pass


def selectJobHunting():
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
