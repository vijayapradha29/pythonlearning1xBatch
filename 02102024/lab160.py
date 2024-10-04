#collections:

from collections import Counter
count=Counter()
list=['red','blue','red','green','blue','blue']
for words in list:
    count=Counter(list)
print(count["green"])

from collections import OrderedDict
d=OrderedDict()
d['a']='A'
d['b']='B'
d['c']='C'
d['d']='D'
for key,value in d.items():
    print(key,value)