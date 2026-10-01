class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} makes a sound"

class Dog(Animal):
    def speak(self):
        base = super().speak()
        return f"{base} barks"

class Puppy(Dog):
    def speak(self):
        base = super().speak()
        return f"{base}, but it's just a small yip"

a = Animal("Generic") 
d = Dog("Rex")
p = Puppy("Max")

print(a.speak()) # Generic Makes a sound
print(d.speak()) # Rex barks
print(p.speak()) # max barks but it's just a small yip

print("---")

# The tricky part: which speak() actually runs?
class Cat(Animal):
    pass   # no speak() defined at all

c = Cat("Whiskers")
print(c.speak())   # what happens here? Whiskers makes a sound