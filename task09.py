f1 = open('input/numbers.txt', 'r')

num = f1.read()
f1.close()

resalt = list(map(int , num.split()))

counts = {}

for n in resalt:
    n_str = str(n).replace('-', '')  
    xonalar_soni = len(n_str)

    if xonalar_soni not in counts:
        counts[xonalar_soni] = 1
    else:
        counts[xonalar_soni] += 1
f2 = open('output/output09.txt', 'w')
f2.write(f"xonalar soni:{counts}")
f2.close()
