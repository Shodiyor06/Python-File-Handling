f = open('input/numbers.txt', 'r')
num = f.read()
f.close()
resalt = sum(map(int , num.split()))

f2 = open('output/output02.txt', 'w')
f2.write(f"totol:{resalt}")
f2.close()