f = open('input/numbers.txt', 'r')
num = f.read()
f.close()
numbers=[]
for i in num.split():
    i = int(i)
    if i % 2 == 0:
        numbers.append(i)

f2 = open('output/output04.txt', 'w')
f2.write(f'juft sonlar {numbers}')
f2.close()