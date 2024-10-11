#break:

for i in range(1,10):
    if i>5:
        break
    print(i)
print("--------------------------------")
#pass:
for i in range(1,10):
    if i==5:
        pass
    else:
        print(i)
print("--------------------------------------")
#continue:
for i in range(1,10):
    if i%2==0:
        continue
    else:
        print(i)
print("------------------------------------------")
#break for i=51:
for i in range(1,101):
    if i==51:
        break
    print(i)

#factorial:
n=5
if n<0:
    print("Factorial is not possible")
else:
    fact=1
    for i in range(1,n+1):
        fact=fact*i
        print(fact)

#fibonacci series:
number=5
a=0
b=1
while a<number:
    print(a,end=' ')
    a,b=b,a + b