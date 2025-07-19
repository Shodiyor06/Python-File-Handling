import csv
from collections import Counter

with open('input/grades.csv', 'r') as csvfile:
    reader = list(csv.reader(csvfile))[1:] 
    grades = [int(row[1]) for row in reader]
    counter = Counter(grades)

    print(counter)
