import csv

# file=open('testdata.csv','r')
# print(file.read())
# file.close()

#or
with open('testdata.csv','r')as file:
    reader=csv.reader(file)
    for row in reader:
        for value in row:
            print(value,end=" ")
        print()