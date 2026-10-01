# Inheritance allows us to inherit attributes and methods from the parents class
# python has 2 builtin function

#isinstance() - tells if an object is an istance of a class
#issubclass() - tells us if a class is a sublass of another

class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def describe(self):
        return f"{self.make} {self.model}"

class Car(Vehicle):
    def __init__(self, make, model, doors):
        super().__init__(make, model)
        self.doors = doors

    def describe(self):
        base = super().describe()
        return f"{base} with {self.doors} doors"

v = Vehicle("Generic", "Model X")
c = Car("Toyota", "Harrier", 4)

print(v.describe()) # Generic Model X
print(c.describe()) # Toyota Harrier 4 doors

print(isinstance(c, Car))       #  True
print(isinstance(c, Vehicle))   # True
print(isinstance(v, Car))       # False

class Motorcycle(Vehicle):
    def __init__(self, make, model):
        super().__init__(make, model)

m = Motorcycle("Honda", "CB500")
print(isinstance(m, Vehicle))    # True
print(isinstance(c, Motorcycle)) #  False