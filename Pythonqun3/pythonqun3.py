file = open("textfile.txt" , "a")
txt = str(input("Entre text:"))
file.write(txt)
file.close()
file = open("textfile.txt" , "r")
print(file.read())