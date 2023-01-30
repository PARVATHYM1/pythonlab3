items = ['Mango', 'Orange', 'Apple', 'Lemon']
file = open('items.txt','w')
for item in items:
    file.write(item+" ")
file.close()