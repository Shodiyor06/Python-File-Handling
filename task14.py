f = open("input/students.txt", 'r')
sdu = f.read()
f.close()

s = sorted(sdu, reverse=True)

f2 = open("output/output14.txt", 'w')
f2.write(f"teskari tartibida:{s}")
f2.close()