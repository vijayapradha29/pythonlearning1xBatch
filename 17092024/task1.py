#right triangle star pattern:
number=input("Enter a Number:\n")
number=int(number)
for i in range(1,number+1):
    if i==1:
        print("*")
    elif i==2:
        print("**")
    elif i==3:
        print("***")
    elif i==4:
        print("****")
    elif i==5:
        print("*****")
    else:
        print("*"*i)