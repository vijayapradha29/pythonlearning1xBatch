#greater than 0:

numbers=[0,-1,3,-50,34,-6,100,-40,23.45]
def greater(numbers):
    return numbers>0

output=list(filter(greater,numbers))
print(output)


products=[
    {"name":"Laptop","Price":1000},
    {"name":"Smartphone","Price":500},
    {"name":"Tablet","Price":300},
    {"name":"Headphones","Price":100}
]
def products1(items):
    return items["Price"]>500
new_out=list(filter(products1,products))
print(new_out)

def products2(items):
    return items["name"]=="Smartphone"
new_out1=list(filter(products2,products))
print(new_out1)


api_response=[
    {"first_name":"Pramod",
     "age":34,
     "total_price":543,
     "last_name":"dutta",
     "email":"pramoddutta{{$random Int}}@live.com",
     "password":"Test@4321",
     "commission":10,
     "roles":[4]},
    {"first_name":"pramod",
     "age":34,
     "total_price":342,
     "last_name":"dutta",
     "email":"pramoddutta{{@randomInt}}@live.com",
     "password":"Test@4321",
     "commission":10,
     "roles":[4]}
]
# print(api_response)
# print(type(api_response))
print(api_response[0])
# print(type(api_response[1]))

def afford(items):
    return items["total_price"]>500
out1=list(filter(afford,api_response))
print(out1)

