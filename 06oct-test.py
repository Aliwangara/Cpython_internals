class Animal:
    def __init__(self, name):
        self.name = name
    def speak(self):
        return f"{self.name} makes a sound"

class Dog(Animal):
    def speak(self):
        return f"{self.name} barks"

class Puppy(Dog):
    def speak(self):
        base = super().speak()
        return f"{base}, but it's just a small yip"

class Cat(Animal):
    pass


animal = Animal("donkey")
print(animal.speak()) # donkey makes a sound
dog = Dog("lelen")
print(dog.speak()) # lelen barks
puppy = Puppy("Rex")
print(puppy.speak()) # Rex barks, but it's just a small yip
cat = Cat("lucky")

print(cat.speak()) # lucky makes a sound