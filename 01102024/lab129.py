class Animal:
    def sound(self):
        print("Animal Sound")
class Dog(Animal):
    # pass
    def sound(self):
        print("Dog Sound")

sound=Animal()
sound.sound()
sound1=Dog()
sound1.sound()