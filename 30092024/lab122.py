#MRO:
class A:
    def greet(self):
        print("Hello from Class A")
class B:
    def greet(self):
        print("Hello from Class B")
class C(A,B):
    pass
class D(B,A):
    pass
obj1=C()
obj1.greet()
obj2=D()
obj2.greet()
print(C.mro())
print(D.mro())