f = open("input/students.txt", 'r')
sdu = f.read()
f.close()
lst = []
for i in sdu.split():
    if i[0] == "A":
        lst.append(i)

f2 = open("output/a_names.txt", 'w')
f2.write(f"a harfdan boshlangan ismlar:{lst}")
f2.close()