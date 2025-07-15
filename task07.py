f = open('input/numbers.txt', 'r')
num = f.read()
f.close()
resalt = list(map(lambda n: int(n)**2, num.split()))

f2 = open('output/output07.txt', 'w')
f2.write(f"darajalari:{resalt}")
f2.close()
