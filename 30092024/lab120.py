#multilevel:
class Father:
    def father_money(self):
        return "5"
class Mother:
    def mother_money(self):
        return "5"
class Son(Father,Mother):
   pass
son_object=Son()
print("The Total Money I have with me is:",int(son_object.father_money())+int(son_object.mother_money()))