# str returns a string with a nicely printable representation of an object, for strings it returns the string itself
# basically the goal of __str__ is to be readable - user friendly for non developer
#  and the goal of __repr__ is to be unambiguous -mostly  meant for developers to find maybe bugs in their codes

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

d1 = Dog("Rex", 3)
print(d1)          # what does this print, by default? <__main__.Dog object at 0x7f8a1c0b3d90> object memory

print("---")

class DogWithStr:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} years old"

d2 = DogWithStr("Bella", 5)
print(d2)           # different now — why? prints(Bella is 5 years old ) because of the str and the return f string

print("---")

class DogWithBoth:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} years old"

    def __repr__(self):
        return f"Dog(name='{self.name}', age={self.age})"

d3 = DogWithBoth("Max", 2)
print(d3)                 # uses which one? uses max is 2 years old
print(str(d3))            # uses which one? uses max is 2 years old
print(repr(d3))           # uses which one? name = "max" , age=2
d3                         # just typing the variable alone (try in a REPL, or use print(repr(d3)) to simulate it)