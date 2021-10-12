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


def setMatchRequirements():
    pass


def selectMatchResult():
    pass
