#collections:
#count,ordereddict:
from collections import Counter
count=Counter()
list=['red','blue','yellow','green','yellow']

# for words in list:
#     count=Counter(list)
#     print(count["green"])
for words1 in list:
    count[words1]+=1
print(count)

from collections import OrderedDict
od=OrderedDict()
od['a']=1
od['b']=2
od['f']=3
od['t']=4
od['d']=5
od['c']=6
print(od)

for keys,values in od.items():
    print(keys,values)