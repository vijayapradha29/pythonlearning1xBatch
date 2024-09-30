#hybrid:
class Vehicles:
    def vehicle(self):
        return "Different Types of Vehicles"
class Bus(Vehicles):
    def bus(self):
        return "I have Bus"
class Lorry(Vehicles):
    def lorry(self):
        return "I have Lorry"
class Transport(Bus,Lorry):
    def transport(self):
        return "I have Bus and as well as Lorry Transport"
object1=Transport()
print(object1.transport())
print(object1.lorry())
print(object1.bus())
print(object1.vehicle())