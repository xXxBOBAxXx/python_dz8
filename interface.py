from from_tasks import read_tasks
from print_tasks import print_all
from print_tasks import print_task
from new_task import to_tasks
from find_task import to_find
from select_task import to_select
from del_task import to_del

def run_program():
    to_end = False
    while not to_end:
        t = read_tasks()
        command = input('выберите команду: 1 - посмотреть задачи, 2 - изменить задачи, 3 - добавить задачи, или другие символы - для выхода: ')
        if command == '1': 
            print_all(t)
            continue
        if command == '2':
            find_id = to_find(t)
            if find_id == None: continue
            elif len(find_id) > 1: 
                id = to_select(t, find_id)
                if id == None: continue
            elif len(find_id) == 1: 
                id = find_id
                print_task(t,id)
            command = input('выберете команду: 1 - отметить задачу выполненной, 2 - удалить задачу, или другие символы - для отмены: ')
            if command == '1' or '2': 
                if command == '': continue
                to_del(t, id, command)
                if command == '1': print('задача отмеченна выполненой')
                if command == '2': print('задача удалена')
            else: continue
        if command == '3': 
            to_tasks()
            print('добавлена новая задача')
            continue
        else: to_end = True
            
