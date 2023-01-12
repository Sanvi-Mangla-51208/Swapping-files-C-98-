

def swappingfiles():
    File1 = input("file 1 name: ")
    File2 = input("file 2 name: ")
    with open(File1,'r') as a:
        data_a = a.read()
    with open(File2,'r') as b:
        data_b = b.read()
    with open(File1,'w') as a:
        a.write(data_b)
    with open(File2,'w') as b:
        b.write(data_a)
swappingfiles()


