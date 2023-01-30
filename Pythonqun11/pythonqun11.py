import os

file_stat = os.stat('file_size.txt')
print(file_stat.st_size)