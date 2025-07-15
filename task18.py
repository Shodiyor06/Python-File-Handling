f = open("input/students.txt", 'r')
sdu = f.read()
f.close()

ism = input("ism kiriting: ")
if ism.title() in sdu:
    print(f"{ism} ismi topildi")
else:
    print("bunday ism topiilmadi")