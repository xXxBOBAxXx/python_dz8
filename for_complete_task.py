import csv

def to_complete(temp):
    with open("complete_tasks.csv", mode="a", encoding='utf-8') as file:
        file_writer = csv.writer(file, delimiter = "-", lineterminator="\r")
        file_writer.writerow(temp)
