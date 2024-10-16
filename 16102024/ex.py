# import csv
# with open('freshdata.csv','r') as file:
#     reader=csv.reader(file)
#     for rows in reader:
#         # print(','.join(rows))
#         print(rows)
#
# import pandas as pd
# df=pd.read_csv("freshdata.csv")
# print(df)
# print(rows[0],rows[1],rows[2],sep='|')

import csv
data=[["Name","Age","City"],["Dhivya",23,"Cuddalore"],["Vijaya",25,"Dubai"],["xyz",23,"abc"]]
# with open('data.csv','w') as file:
#     write=csv.writer(file)
#     for rows1 in data:
#         write.writerow(rows1)
#
# file=open('data.csv','r')
# print(file.read())
# file.close()

temp_data=[]
with open("data.csv",'r') as file:
    reader=csv.reader(file)
    for rows in reader:
        temp_data.append(rows)
temp_data[2][1]=35
# print(temp_data)
with open("data.csv",'w',newline='') as csvfile:
    writer=csv.writer(csvfile)
    writer.writerows(temp_data)
    print(temp_data)