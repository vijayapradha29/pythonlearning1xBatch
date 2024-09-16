#break in loops:
#need to print the numbers from 0 to 10 but i dont want to print after 5 then use break
count=0
while count<=10:
    print(count)
    if count>=5:
        break
    count=count+1

#or using for loop
for counter in range(1,10):
    if counter>=5:#counter==5
        break
    print(counter)
print("End of For Loop")