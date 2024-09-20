#maps and filters
square=lambda x:x*x
print(square(5))
#or
numbers=[1,2,3,4,5]
square_numbers=[]
for i in numbers:
    square_numbers.append(square(i))
print(square_numbers)
#or
square_numbers2=list(map(lambda x:x*x,numbers))
print(square_numbers2)

#map can take lambda abd as well as other functions also

def threetriple(a):
    return a*3
triple_number=list(map(threetriple,numbers))
print(triple_number)