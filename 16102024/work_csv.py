import csv
with open('testdata12.csv','r') as file:
    reader=csv.reader(file)
    for rows in reader:
        for values in rows:
            print(values,sep="------>")
            print()