import csv
from for_complete_task import to_complete

def to_del(t, id, command):
    with open("tasks.csv", mode="w", encoding='utf-8') as file:
        file_writer = csv.writer(file)
    with open("tasks.csv", mode="w", encoding='utf-8') as file:
        file_writer = csv.writer(file, delimiter = "-", lineterminator="\r")
        temp = []
        temp = t[id]
        t.pop(id)
        for i in t:
            file_writer.writerow(i)
        if command == '1': to_complete(temp)
