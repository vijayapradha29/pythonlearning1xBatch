#Leap year calculator:
year=int(input("Enter the Year:\n"))
if (year%4==0):
    # print("Leap Year")
    if (year%100==0):
    # print("Not a Leap Year")
        if (year % 400 == 0):
            print("Leap Year")
        else:
            print("Not a Leap Year")
    else:
        print("Leap Year")
else:
    print("Not Leap Year")
# if (year%400)==0 or  (year%100)!=0 and (year%4)==0:
#     print("Leap Year")
# else:
#     print("Not a Leap Year")


