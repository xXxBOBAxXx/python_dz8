import csv

def to_tasks():
    with open("tasks.csv", mode = "a", newline = '', encoding='utf-8') as file:
        file_writer = csv.writer(file, delimiter = "-")
        t = ['', ''] 
        t[0] = input('Введите описание задачи: ') 
        t[1] = input('Контрольную дату задачи: ') 
        file_writer.writerow(t)
