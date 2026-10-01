# MRO - method resolution order - determines how python searches for methods and attributes
#multiple inheritance allows a class to inherit from more than one parent class


class Swimmer:
    def move(self):
        return "swimming"

class Walker:
    def move(self):
        return "walking"

class Duck(Swimmer, Walker):
    pass

d = Duck()
print(d.move())   # which one wins — Swimmer's or Walker's? Walker

print("---")

print(Duck.__mro__)   # the actual search order, spelled out

print("---")

# Now with Walker listed first instead
class Duck2(Walker, Swimmer):
    pass

d2 = Duck2()
print(d2.move())   # does the order matter? No