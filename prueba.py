my_file = open("hola")
line = my_file.readlines()
for lin in line:
    print(lin.rstrip('\n'))