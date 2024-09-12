#Identity Operator:
#is returns True if both variables are the same object
#is not returns True if both variables are not the same object

x=[1,2,3]
y=[1,2,3]
print(x is y)
print(id(x))
print(id(y))
print(x is not y)