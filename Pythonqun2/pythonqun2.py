file = open("file.txt" , "r")
n = int(input("How many lines want to display:"))
if n <=0 :
    print("please entre the positive value")
else:
    for i in range(n):
        line = file.readline()
        print(line)