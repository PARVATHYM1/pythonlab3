file = open("name.txt" , "r")
open_file = file.readlines()
for s in open_file:
        print(s.strip())