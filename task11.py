f = open("input/students.txt", 'r')
sdu = f.read()
f.close()

f2 = open("output/output11.txt", 'w')
f2.write(sdu)
f2.close()
