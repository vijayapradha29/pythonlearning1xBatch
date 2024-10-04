#read line by line:

with open("read.txt",'r') as file:
    line=file.readline()
    print(line)
print("-------------------------------------------------")
#read all the lines in a file:
with open("read.txt",'r') as file1:
    lines=file1.readlines()
    print(lines)