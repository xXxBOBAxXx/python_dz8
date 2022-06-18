from from_tasks import t
from print_tasks import print_all
from new_task import to_tasks
from find_task import to_find
from select_task import to_select
from del_task import to_del
from for_complete_task import to_complete

def run_program():
    to_end = False
    while not to_end:
        command = input('выберите команду: 1 - посмотреть задачи, 2 - изменить задачи, 3 - добавить задачи, или другие символы - для выхода: ')
        if command == '1': print_all(t)
        elif command == '2':
            find_id = to_find(t)
            if len(find_id) > 1: id = to_select(t, find_id)
            elif len(find_id) == 1: id = find_id
            else: run_program()
            command = input('выберете команду: 1 - отметить задачу выполненной, 2 - удалить задачу, или другие символы - для отмены: ')
            if command == '1' or '2': to_del(t, id, command)
            else: run_program()
        elif command == '3': to_tasks()
        else: to_end = True