f = open("input/students.txt", 'r')
sdu = f.read()
f.close()
soni = 0
for i in sdu.split():
    soni+=1
f2 = open("output/output12.txt", 'w')
f2.write(f"isimlar soni:{soni}")
f2.close()