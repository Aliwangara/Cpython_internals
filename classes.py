class Dog:
    species = "Canis familiaris"   # class attribute — shared by all dogs

    def __init__(self, name, age):
        self.name = name           # instance attribute — unique per dog
        self.age = age

    def bark(self):
        print(f"{self.name} says woof!")

d1 = Dog("Rex", 3)
d2 = Dog("Bella", 5)

d1.bark()
d2.bark()

print(d1.name, d2.name)          # different, obviously
print(d1.species, d2.species)    # Same species because it is inside a dog class itself not in any methods

print("---")

# The interesting part — what happens if you change a class attribute?
Dog.species = "Canis lupus familiaris"
print(d1.species, d2.species)    # did BOTH change? yes both changes because they share the same instance

print("---")

# vs changing an instance attribute
d1.name = "Max"
print(d1.name, d2.name)          # did both change this time? No because they have different instance