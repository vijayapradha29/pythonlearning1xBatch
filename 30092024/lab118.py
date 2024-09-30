class Grandparent:
    def grandparent_method(self):
        return "Grandparent's Method"
class Parent(Grandparent):
    def parent_method(self):
        return "Parent's Method"
class Child(Parent):
    def child_method(self):
        return "Child's Method"
child_object=Child()
print(child_object.grandparent_method())
print(child_object.parent_method())
print(child_object.child_method())