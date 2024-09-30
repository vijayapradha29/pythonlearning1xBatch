# if son and father has no cars:
class Gf:
    def cars(self):
        return "Old Car"
class F(Gf):
    pass
class S(F):
    pass
son=S()
print(son.cars())