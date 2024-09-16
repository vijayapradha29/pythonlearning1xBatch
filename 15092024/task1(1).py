#factorial:
# n!=n*(n-1)*(n-2)............
# number=int(input("Enter the Number:\n"))
# num=1
# for i in range(1,number+1):
#     # print(num)
#     num=num*i
# print(num)

#or
number=int(input("Enter the Number:\n"))
if number<0:
    print("Factorial is not possible")
else:
    fact=1
    for i in range(1,number+1):
        fact=fact*i
print("Factorial is----->",fact)
