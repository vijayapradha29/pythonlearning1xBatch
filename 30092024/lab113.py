#inheritance:
class animal:
    def speak(self):
        pass
class dog(animal):
    def speak(self):
        print("Dog speaks Bow bow")
dog_object=dog()
dog_object.speak()