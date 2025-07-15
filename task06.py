f = open('input/numbers.txt', 'r')
num = f.read()
f.close()
numbers=[]
for i in num.split():
    i = int(i)
    if i % 2 != 0:
        numbers.append(i)

f2 = open('output/odd_numbers.txt', 'w')
f2.write(f'toq sonlar {numbers}')
f2.close()