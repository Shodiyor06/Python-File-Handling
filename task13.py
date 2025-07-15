f = open("input/students.txt", 'r')
sdu = f.read()
f.close()

s = sorted(sdu)

f2 = open("output/output13.txt", 'w')
f2.write(f"alifbo tartibida:{s}")
f2.close()