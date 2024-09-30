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
print(son.cars())