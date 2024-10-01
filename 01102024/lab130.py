#suppose if we want to call parent function from or by using child function then use super().functionname of parent()
class Animal:
    def sound(self):
        print("Animal Sound")
class Dog(Animal):
    # pass
    def sound(self):
        super().sound()
        print("Dog Sound")

# sound=Animal()
# sound.sound()
sound1=Dog()
sound1.sound()