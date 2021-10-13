def demand_choice():
    choices = {
        '0': {
            'name': '設定求職需求',
            'func': set_job_hunting,
        },
        '1': {
            'name': '查詢求職結果',
            'func': select_job_hunting,
        }
    }

    for i in choices:
        print(f'{i}: {choices[i]["name"]}')
    choice = input('請選擇 ...')
    choices[choice]['func']()


def set_job_hunting():
    pass


def select_job_hunting():
    pass
