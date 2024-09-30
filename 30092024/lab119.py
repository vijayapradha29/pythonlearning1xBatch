#hierarchical:
class Father:
    def parent(self):
        return "I have Car and Bicycle."
class Son(Father):
    def i_want(self):
        return "Father,I want Car."
class Daughter(Father):
    def i_also_want(self):
        return "Father,I want Bicycle."
object1=Son()
print(object1.parent())
print(object1.i_want())
object2=Daughter()
print(object2.parent())
print(object2.i_also_want())