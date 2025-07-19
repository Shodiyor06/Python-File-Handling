import csv
with open('input/grsdes.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    print(list(reader))


