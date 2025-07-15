f1 = open('input/numbers.txt', 'r')
num = f1.read()
f1.close()

resalt = list(map(int , num.split()))
s=sorted(resalt)
f2 = open("output/sorted_numbers.txt", "w")
f2.write(' '.join(map(str, s)))