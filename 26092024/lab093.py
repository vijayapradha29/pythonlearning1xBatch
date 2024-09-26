#attributes:

class Person:
    name=None
    age=None
    phone_number=None
    gender=None
    height=None
    weight=None
    profession=None

    def talk(self):
        print("Talk")
    def walk(self):
        print("Walk")
    def sleep(self):
        return "Am Sleeping"

amit_object=Person()
amit_object.name="Amit"
amit_object.age=23
amit_object.phone_number="9876543210"

print(amit_object)
amit_object.talk()

divya_object=Person()
divya_object.name="Divya"
divya_object.gender="Female"
divya_object.height=134.00
divya_object.weight=67
divya_object.age=23
divya_object.profession="student"
divya_object.walk()
divya_object.sleep()
