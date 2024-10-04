#write to csv file:
import csv
data=[["Name","Age","City"],["Dhivya",23,"Cuddalore"],["Vijaya",25,"Dubai"]]

with open("data.csv",'w') as file:
    write=csv.writer(file)
    for row in data:
        write.writerow(row)