#string-Bunch of Characters
name="Vijaya"

#String Functions
#capitalize:
name1=name.capitalize()
print(name1)

#upper:
name=name.upper()
print(name)

#id
print(id(name))

#lowercase
result=name.lower()
print(result)
print(id(result))

#swapcase:->converts upper to lower case and lower to uppercase

new_name="vIjAyA"
print(new_name.swapcase())

#title
heading="hi,how are you?"
print(heading.title())

t1="dutta ji"
t2="pramod ji"
print(t1.capitalize())
print(t2.upper())

#replace
text="hello world"
result=text.replace("world","python")
print(result)


#length and index
name="pramod"
#len->starts from 1
print(len(name))
#index->starts from 0 to length-1
#p-0,r-1,a-2,m-3,o-4,d-5

#find:
text="hello,how are you?"
x=text.find("h")
print(x)
y=text.find("z")
print(y)

#count:
c=text.count("how")
print(c)
f=text.count("why")
print(f)

#string immutability:
#use id method to verify it
str1="pramod"
print(id(str1))
str1="dutta"
print(id(str1))


