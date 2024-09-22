t=("TheTestingAcademy","For","TheTestingAcademy")
print("\n Set with the use of tuples:")
print(set(t))
#union:
set1={1,2,3}
set2={4,5,6}
sets=set1.union(set2)
print(sets)
#intersection:
set1={1,2,3,4,5}
set2={4,5,6,7,8}
sets=set1.intersection(set2)
print(sets)
#differnce:
set1={1,2,3,4,5}
set2={4,5,6,7,8}
sets=set1.difference(set2)
print(sets)
#or
sets=set2.difference(set1)
print(sets)

my_set={1,23.45,"Vijaya",True}
print(my_set)
my_set2={0,True,1,False}
print(my_set2)

#subset:
se1={1,2,3,4,5,6}
se2={2,3,6,7}
subset=se2.issubset(se1)
print(subset)

#iterate in set:
set1=set(["TheTestingAcademy","For","Thetestingacademy"])
print(set1)
for i in set1:
    print(i)

new_set={1,2,3,4,5,6,7,8,9,10}
new_set.remove(5)
print(new_set)