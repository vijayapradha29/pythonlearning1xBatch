class A:
    def print(self):
        print("A")
class B(A):
    def print1(self):
        print("B")
class C(A):
    def print2(self):
        pass

a=A()
a.print()
b=B()
b.print1()
c=C()
c.print2()
# print(c.print())