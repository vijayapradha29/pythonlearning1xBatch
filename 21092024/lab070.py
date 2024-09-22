#how to create tuples
# 2 ways
tuple1=()
tuple2=(1,2,3,4,5,6)
tuple3=tuple((11,12,11,12,13))
print(tuple1)
print(tuple2)
print(tuple3)

#we can use tuple to store different urls whose values will not be changed while its in production as
endpoints=("https://restful-booker.herokuapp.com/auth","https://restful-booker.herokuapp.com/auth","https://restful-booker.herokuapp.com/auth")
print(endpoints)
#you can access:
print(endpoints[0])
#you cannot change:
# endpoints[1]="https://restful-booker.herokuapp.com/auth"
# print(endpoints)
#delete tuple
del tuple1
# print(tuple1)