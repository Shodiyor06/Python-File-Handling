f = open('input/numbers.txt', 'r')
num = f.read()
f.close()
resalt = list(filter(lambda n: int(n) % 5 == 0, num.split()))

f2 = open('output/output08.txt', 'w')
f2.write(f"5 ga bulinadigan:{resalt}")
f2.close()

