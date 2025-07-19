import csv
with open('input/grades.csv', 'r') as csvfile:
    reader = list(csv.reader(csvfile))
    u_q = 0
    for i in reader[1:]:
        u_q += int(i[1])
    svg = u_q / len(reader[1:])
    print(f"urta qiymati:{svg}")
    