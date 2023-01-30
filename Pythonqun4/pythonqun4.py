n = int(input("Entre n lines:"))
file = open("text.txt" , "r")
for line in (file.readlines() [-n:]):
    print(line, end="")
file.close()