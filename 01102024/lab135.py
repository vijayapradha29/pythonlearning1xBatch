#abstraction:
from abc import ABC,abstractmethod
class Car(ABC):
    @abstractmethod
    def moveforward(self):
        pass
    @abstractmethod
    def movebackward(self):
        pass
    @abstractmethod
    def fm(self):
        pass
class Swift(Car):
    def moveforward(self):
        print("Swift is moving Forward")
    def movebackward(self):
        print("Swift is moving Backward")
    def fm(self):
        print("Swift is playing FM")
class Innova(Car):
    def moveforward(self):
        print("Innova is moving Forward")
    def movebackward(self):
        print("Innova is moving Backward")
    def fm(self):
        print("Innova is playing FM")

s=Swift()
s.moveforward()
i=Innova()
i.movebackward()
