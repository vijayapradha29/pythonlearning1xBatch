#if we want to update particular row:
import csv

temp_data=[]
id_update=2
new_age=24

with open("testdata.csv",'r') as csvfile:
    reader=csv.reader(csvfile)
    for row in reader:
        temp_data.append(row)

temp_data[2][1]=24
print(temp_data)

with open("testdata.csv",'w',newline='') as csvfile:
    writer=csv.writer(csvfile)
    writer.writerows(temp_data)
