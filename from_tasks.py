import csv

def read_tasks():
    t = []
    with open("tasks.csv", encoding = 'utf-8') as file:
        reader = csv.reader(file, delimiter = "-")
        for i in reader:
            t.append(i)
        return t
