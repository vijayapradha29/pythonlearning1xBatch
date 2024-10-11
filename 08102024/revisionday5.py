#arithmetic operators:+,-,*,/,%,**,//
a=5
b=10
c=a+b
d=a-b
e=a*b
f=a/b
g=a%b
h=a**b
i=a//b
print(c,d,e,f,g,h,i)

#logical operators:and,or,not
a=False
b=True
c=a and b
d=a or b
e=not a
print(c)
print(d)
print(e)

#comparison operators:<,>,<=,>=,==,!=
a=5
b=7
print(a<b)
print(a>b)
print(a<=b)
print(a>=b)
print(a==b)
print(a!=b)

#assignament operators:+=,-=,*=,/=,%=,**=,//=,==
a=1
b=3
a+=b
print(a)
a-=b
print(a)
a*=b
print(a)
a/=b
print(a)
a%=b
print(a)
a**=b
print(a)
a//=b
print(a)
print(a==b)

#membership operators:in,not in
a=[1,2,3]
b=[1,2,3]
print(3 in a)
print(4  not in b)

#identity operators:is,is not
a=[1,2,3]
b=[1,2,3]
print(a is not  b)

a=[1,2,3]
b=a
print(a is b)

#unary:
#unary plus:
a=5
print(a)
#unary minus:
b=10
print(-b)
a=True
print(not a)

#ternary operators:
#true_value if condition else false_value
a=5
b=5
result="a is equal to b" if a==b else "a is greater than or less than b"
print(result)



