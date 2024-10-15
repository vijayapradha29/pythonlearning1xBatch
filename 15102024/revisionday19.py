#bank account:
# class Bank:
#     def __init__(self):
#         self.balance=0
#     def deposit(self,amount):
#         self.balance=self.balance+amount
#     def withdraw(self,amount):
#         self._balance=self.balance-amount
#     def check_balance(self):
#         self.__balance=self._balance
#         print("Your Balance is:",self.__balance)
#     def is_authenticated(self,isAuth):
#         if isAuth:
#             self.check_balance()
#         else:
#             print("You are not Authenticated")
# bank1=Bank()
# bank1.deposit(1000)
# bank1.withdraw(500)
# # bank1.check_balance()
# bank1.is_authenticated(True)
#
# #using getter,setter:
# class Person:
#     def __init__(self,name,age):
#         self._age=age
#         self.__name=name
#     def print_details(self):
#         print("Your Details are:",self.__name,self._age)
#     def get_name(self):
#         return self.__name
#     def set_name(self,name):
#         self.__name=name
# dhivya=Person("Dhivya",23)
# jagan=Person("Jagan",26)
# dhivya.set_name("Vijaya")
# name=dhivya.get_name()
# print(name)
# dhivya.print_details()
# # dhivya=Person("Dhivya",23)
# # jagan=Person("Jagan",26)
# # dhivya.print_details()
# # jagan.print_details()
# jagan.set_name("JAGAN")
# name1=jagan.get_name()
# print(name1)
# jagan.print_details()
#
# #password:
# class Pass:
#     def __init__(self,password):
#         self.__password=password
#     def print_password(self):
#         password=len(self.__password)
#         # print("Your Password is:",password)
#     def get_pass(self):
#         return self.__password
#     def set_pass(self,password):
#         self.__password=password
#         # if len(self.__password)>5:
#         #     print("Your Password is:",self.__password)
#         # else:
#         #     print("Weak Password")
#     def isAuth(self,isAuth):
#         if isAuth:
#             print("Your Password length is:",len(self.__password),"and Your Password is:",self.__password)
#         else:
#             print("You are not Authenticated")
# pass1=Pass("hacker123")
# # pass1.print_password()
# pass1.set_pass("123")
# # pwd=pass1.get_pass()
# # print(pwd)
# pwd=pass1.isAuth(False)
# # pass1.isAuth(True)
#
#
# #car:
# class Cars:
#     def __init__(self,name,model,colour):
#         self._name=name
#         self.__model=model
#         self.colour=colour
#
#     def car_details(self):
#         print("Your Car Details are:",self.colour,self.__model,self._name)
#
#     def get_car(self):
#         return self._name
#         # return self.__model
#     def set_car(self,name):
#         self._name=name
#
#
#
# car_object1=Cars("Figo","I20","Black")
# # car_object1.car_details()
# car_object1.set_car("Toyota")
# car12=car_object1.get_car()
# print(car12)
# car_object1.car_details()
#
#
# #single inheritance:
#
# class Animals:
#     def speak(self):
#         print("Animals dont speak")
#         # pass
# class Dog(Animals):
#     # def speak(self):
#         pass
#         # print("Dog barks")
#
# dog_object=Dog()
# dog_object.speak()
#
# #multiple inheritance:
# class Grandfather:
#     def properties(self):
#         return "Grandfather's Properties"
# class Father(Grandfather):
#     pass
#     # def properties(self):
#     #     return "Father's Properties"
# class Son(Father):
#     pass
#     # def properties(self):
#     #     return "Son's Properties"
#
# father=Father()
# son=Son()
# grandfather=Grandfather()
# print(grandfather.properties())
# print(father.properties())
# print(son.properties())
#
# #heirarchial inheritance:
#
# class Father:
#     def vehicles1(self):
#         return "It's Fathers Vehicle"
# class Son(Father):
#     def vehicles2(self):
#         return "It's Sons Vehicle"
# class Daughter(Father):
#     def vehicles3(self):
#         return "It's Daughters Vehicle"
# daughter=Daughter()
# son=Son()
# print(son.vehicles1())
# print(son.vehicles2())
# father=Father()
# print(daughter.vehicles3())
# print(daughter.vehicles1())
#
# #multiple inheritance:
# class Father:
#     def amount(self):
#         print("i gave 5 rupees to my son")
# class Mother:
#     def amount(self):
#         print("i gave 5 rupees to my son")
# class Son(Father,Mother):
#     def amount(self):
#         print("I got 5 rupees from my father and as well as from my mother")
#
# son=Son()
# # son.amount()
# son.amount()
# Mother().amount()
#hybrid inheritance:

# class A:
#     def methoda(self):
#         return "Am from method A"
# class B(A):
#     def methodb(self):
#         return "am from method B"
# class C(A):
#     def methodc(self):
#         return "am from method c"
# class D(B,C):
#     def methodd(self):
#         return "am from method D"
#
# d=D()
# print(d.methodd())
# print(d.methodc())
# print(d.methodb())
# print(d.methoda())

class A2:
    def greet(self):
        print("Hello from class A")
class B2(A2):
    def greet(self):
        print("Hello from class B")
class C2(A2,B2):
    pass
class D2(B2,A2):
    pass

d=D2()
d.greet()
print(D2.mro())