def supply_choice():
    # raise Exception('Error: object "supply_choice" not found')

    choices = {
        '0': {
            'name': '設定媒合需求',
            'func': set_match_requirements,
        },
        '1': {
            'name': '查詢媒合結果',
            'func': select_match_result,
        }
    }

    for i in choices:
        print(f'{i}: {choices[i]["name"]}')
    choice = input('請選擇 ...')
    choices[choice]['func']()


def set_match_requirements():
    position = input('請輸入欲招募的職位')
    number = input('請輸入欲招募的人數')
    num_limit = input('請輸入媒合人數上限')
    return {'position': position, 'number': number, 'num_limit': num_limit}


def select_match_result():
    pass
