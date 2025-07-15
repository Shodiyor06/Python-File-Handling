f = open('input/numbers.txt', 'r')
num = f.read()
f.close()
numbers = []
for n in num.split(','):
    n = n.strip() 
    
    numbers.append(n)

resalt = max(numbers)

f2 = open('output/output03.txt', 'w')
f2.write(f"max son:{resalt}")
f2.close()