import csv
with open('input/grades.csv', 'r') as csvfile:
    reader = list(csv.reader(csvfile))
    lst = []
    for i in reader[1:]:
        if int(i[1]) == 5:
            lst.append(i)
with open('output/five_grades.csv', 'w') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(lst)
    print(f"bahosi 5 bo'lgan talabalar: {lst}")
        