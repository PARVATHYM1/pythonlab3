with open("file.txt" , "r") as f:
    lines = len(f.readlines())
    print("Total numbetr of lines:" , lines)