#dictionary:
#another type of datatype in python
my_dict={}
my_dict2=dict()
print(type(my_dict))
print(type(my_dict2))

phone_book={"Batman":987654321,"Superman":1234567890,"Wonderwoman":7678356854}
print(phone_book)
print(len(phone_book))
print(phone_book["Batman"])
print(phone_book["Wonderwoman"])

phone_book2=dict(batman=123,cersei=342,GB=323)
print(phone_book2)
print(phone_book2['GB'])
# #or
print(phone_book2["GB"])
# #or
print(phone_book2.get('GB'))
#or
print(phone_book2.get("GB"))


