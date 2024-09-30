class Gf:
    def cars(self):
        return "Old Car"
class F(Gf):
    def cars(self):
        return "Honda Civic"
class S(F):
    def cars(self):
        return "Lambo"
son=S()
grand=Gf()
father=F()
print(son.cars())
print(grand.cars())
print(father.cars())