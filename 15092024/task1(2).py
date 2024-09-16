#fibonacci series:
number=int(input("Enter the Number:\n"))
a=0
b=1
while a<number:
    print(a,end=" ")
    a,b=b,a+b