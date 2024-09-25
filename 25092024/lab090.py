api_response = [
    {
    "first_name": "Pramod",
    "age": 34,
    "total_price":543,
    "last_name": "Dutta",
    "email": "pramoddutta{{$randomInt}}@live.com",
    "password": "Test@4321",
    "commission": 10,
    "roles": [
        4
    ]
},
    {

    "first_name": "Pramod",
    "age": 34,
    "total_price":342,
    "last_name": "Dutta",
    "email": "pramoddutta{{$randomInt}}@live.com",
    "password": "Test@4321",
    "commission": 10,
    "roles": [
        4
    ]
}]
print(type(api_response))
print(type(api_response[0]))

def is_affordable(items):
    # print(items["first_name"])
    return items["total_price"]<500


affordable=list(filter(is_affordable,api_response))
print(affordable)
print(affordable[0]["first_name"]+str(affordable[0]["age"]))
