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


def setJobHunting():
    pass


def selectJobHunting():
    pass
