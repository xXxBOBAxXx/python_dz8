from print_tasks import print_select

def to_select(t, find_id):
    for id in find_id:
        print_select(t,id)
    id = int(input('выберете номер нужной задачи, любой другой символ - отмена: '))
    if id in find_id:
        if type(id) == int:
            return int(id)
    else: return None
