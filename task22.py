import csv
with open('input/grades.csv', 'r') as csvfile:
    reader = list(csv.reader(csvfile))[1:]
    y=0
    for i in reader:
        if i[1] == '5':
            y+=1
    print(f"5 balli talabalar soni: {y}")
