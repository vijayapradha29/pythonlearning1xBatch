#inheritance:
class animal:
    def speak(self):
        pass
    def car(self):
        print("Lamborgini")
class dog(animal):
    def speak(self):
        print("Dog speaks Bow bow")
    def i_want_drive(self):
        animal().car()
dog_object=dog()
dog_object.speak()
dog_object.i_want_drive()