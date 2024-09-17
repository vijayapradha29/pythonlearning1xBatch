#lambda function:
from tkinter.font import names


def sayhello(name):
    print("Hi your name is",name)

sayhello("Vijaya")

output=lambda name:print("Hi your name is",name)
output("Pradha")
