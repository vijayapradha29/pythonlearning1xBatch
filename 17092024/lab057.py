#sum:
number=int(input("Enter Your Number:\n"))
sum=0
while number!=0:
    digit=number%10
    sum=sum+digit
    number=int(number/10)
print(sum)