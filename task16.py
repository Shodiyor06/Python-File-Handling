f = open("input/students.txt", 'r')
sdu = f.read()
f.close()
lst = []
for i in sdu.split():
    if len(i) > 5:
        lst.append(i)

f2 = open("output/output16.txt", 'w')
f2.write(f"5 dan uzun ismlar:{lst}")
f2.close()