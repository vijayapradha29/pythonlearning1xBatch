#find the maximum of three numbers:
a=10
b=20
c=13
max=None #or 0(zero)
if a>b and a>c:
    max=a
elif b>c and b>a:
    max=b
else:
    max=c
print(max)