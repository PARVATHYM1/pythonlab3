with open ("test.txt") as f1 , open ("text.txt") as f2:
    for line1, line2 in zip(f1,f2):
        print(line1+line2)