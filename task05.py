f = open('input/numbers.txt', 'r')
num = f.read()
f.close()
avg = sum(map(int , num.split())) / len(num)

f2 = open('output/output05.txt', 'w')
f2.write(f"urta qiymat: {avg}")
f2.close()