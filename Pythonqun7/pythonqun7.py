file = open("text.txt", "r")
array = []
for line in file:
    array.append(line.strip())
    
    
print(array)