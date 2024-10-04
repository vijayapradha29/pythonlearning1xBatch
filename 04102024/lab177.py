import csv
with open("testdata.csv",'r') as  csvfile:
    reader=csv.reader(csvfile)
    for row in reader:
        print(','.join(row))
        #or
        print(row)