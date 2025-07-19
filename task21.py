import csv
with open('input/grades.csv', 'r') as csvfile:
    reader = list(csv.reader(csvfile))[1:]
    print(max(reader, key=lambda x: int(x[1])))
