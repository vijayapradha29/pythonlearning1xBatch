# if son has no cars:
class Gf:
    def cars(self):
        return "Old Car"
class F(Gf):
    def cars(self):
        return "Honda Civic"
class S(F):
    pass
son=S()
print(son.cars())