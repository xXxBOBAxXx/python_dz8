from print_tasks import print_select

def to_select(t, find_id):
    for id in find_id:
        print_select(t,id)
    id = input('выберете номер нужной задачи, любой другой символ - отмена: ')
    if type(id) != int: return None
    if id in find_id: return id
    else: return None
    
