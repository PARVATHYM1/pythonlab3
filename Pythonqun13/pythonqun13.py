with open("first.txt" , "r") as file1 , open("second.txt" , "w") as file2:
    for line in file1:
        file2.write(line)
