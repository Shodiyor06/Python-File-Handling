f = open("input/students.txt", 'r')
sdu = f.read()
f.close()
h_soni = {}
for i in sdu.split():
    if i not in h_soni:
        h_soni[i] = len(i)
    else:
        h_soni[i] = len(i)

f2 = open("output/output15.txt", 'w')
f2.write(f"harflar soni:{h_soni}")
f2.close()