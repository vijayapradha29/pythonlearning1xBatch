tuple1=tuple(["vijaya","Pradha"])
print(tuple1)
print(tuple1[0])
print(tuple1[1])

#merging tuples:
hero1=("Batman","Bruce Wayne")
hero2=("Wonder woman","Diana prince")
awesome_team=hero1+hero2
print(awesome_team)

#convert tuple to list:
my_tuple=(1,2,3,4,5,6,7)
print(list(my_tuple))

#how to assign values in tuple:
q,w,e=(45,56,78)
print(q)
print(w)
print(e)

#nested tuple:
hero1=("Batman","Bruce wayne")
hero2=("Wonder woman","Diana prince")
awesome=(hero1,hero2)
print(awesome)

#merging list:
list1=[1,2,3,4,5]
list2=["a","b","c","d","e"]
lists=list1+list2
print(lists)

#search in tuple:
cities=("London","Paris","Los angeles","Tokyo")
print("Paris" in cities)
print("Moscow" in cities)