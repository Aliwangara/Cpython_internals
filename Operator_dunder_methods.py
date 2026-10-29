 
print(1+2) # uses a background method called __add__
print(int.__add__(1,2)) # 3 adds the two together
print(str.__add__("ali", "wangara")) # aliwangara

# we can use it to add two value of different boject together

# eg:

def __add__(self,other):
    return self.pay + other.pay

# so when you add two objects together eg print(abject1 + object 2) it gives you the pay total


#len dunder method
print(len("test")) # 4 uses the background __len__
print("test".__len__()) # 4


class Vec:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vec(self.x + other.x, self.y + other.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __len__(self):
        return 2

    def __repr__(self):
        return f"Vec({self.x}, {self.y})"

a = Vec(1, 2)
b = Vec(1, 2)
c = a + b
print(c) # 2, 4
print(a == b) #true
print(a is b) # false
print(len(a)) # 2

class Plain:
    def __init__(self, x):
        self.x = x

p1 = Plain(1)
p2 = Plain(1)
print(p1 == p2) #false