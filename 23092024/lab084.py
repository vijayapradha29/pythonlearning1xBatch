api_response = {
    "first_name": "Pramod",
    "age": 34,
    "last_name": "Dutta",
    "email": "pramoddutta{{$randomInt}}@live.com",
    "password": "Test@4321",
    "commission": 10,
    "roles": [
        4
    ]
}

api_response["age"]=54
dictionary=dict(api_response)
print(dictionary)
print(type(api_response))

print(api_response.get('password'))

print(api_response['roles'])
print(api_response.get('roles'))
for keys,values in dictionary.items():
    print(keys,values)