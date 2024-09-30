#inheritance:
class animal:
    def speak(self):
        print("Animal Speak")
class dog(animal):
    pass
    # def speak(self):
    #     print("Dog speaks Bow bow")
dog_object=dog()
dog_object.speak()