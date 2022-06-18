from from_tasks import t
from print_tasks import print_all
from new_task import to_tasks
from find_task import to_find
from select_task import to_select
from del_task import to_del

def run_program():
    to_end = False
    while not to_end:
        command = input('выберите команду: 1 - посмотреть задачи, 2 - изменить задачи, 3 - добавить задачи, или другие символы - для выхода: ')
        if command == '1': 
            print_all(t)
            run_program()
        if command == '2':
            find_id = to_find(t)
            if find_id == None: run_program()
            if len(find_id) > 1: 
                id = to_select(t, find_id)
                if id == None: run_program()
            if len(find_id) == 1: id = find_id
            command = input('выберете команду: 1 - отметить задачу выполненной, 2 - удалить задачу, или другие символы - для отмены: ')
            if command == '1' or '2': to_del(t, id, command)
            run_program()
        if command == '3': 
            to_tasks()
            run_program()
        else: to_end = True
