#readlines to remove list:
with open("read.txt",'r') as file1:
    lines=file1.readlines()
    print(lines)
    for line in lines:
        print(line,end='')