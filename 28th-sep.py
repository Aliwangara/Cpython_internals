# import dis

# def total_price(price, qty):
#     subtotal = price * qty
#     return subtotal

# dis.dis(total_price)


# a = [1,2,3,4,5]
# b = [1,2,3,4,5]
# c=a

# x =None

# print(a==b) # True
# print(a is b) # False
# print(f"a id is {id(a)}. b id is: {id(b)}") # a id is 2154328973376. b id is: 2154329121536
# print(c is a) # True
# print(x is None)


# def add_with_append(lst):
#     lst.append(99) #predicted [99]
#     print("inside:", lst, id(lst))

# my_list = [1, 2, 3]
# print("before:", my_list, id(my_list))
# add_with_append(my_list)
# print("after: ", my_list, id(my_list))


# def add_with_iadd(lst):
#     lst += [99] # works same as .appends extends the list
#     print("inside:", lst, id(lst))

# my_list = [1, 2, 3]
# print("before:", my_list, id(my_list))
# add_with_iadd(my_list)
# print("after: ", my_list, id(my_list))

# def add_with_plus(lst):
#     lst = lst + [99] # creates a new object lst = [99]
#     print("inside:", lst, id(lst))

# my_list = [1, 2, 3]
# print("before:", my_list, id(my_list))
# add_with_plus(my_list)
# print("after: ", my_list, id(my_list))

# def add_with_n_function(n):
#     n+=1
#     print(f"Inside: {n} {id(n)}")

# x = 5

# print(f"Before {x} {id(x)}")

# add_with_n_function(x)

# print(f"After:{x} {id(x)}")


# import sys

# a = [1, 2, 3]
# b = a
# container = [a]

# print(sys.getrefcount(a)) # 4

# # del b
# print(sys.getrefcount(a)) # 3

# # del container
# print(sys.getrefcount(a)) # 2

# class Demo:
#     def __del__(self):
#         print("Demo destroyed")

# d1 = Demo()
# d2 = d1

# print(sys.getrefcount(d1))

# del d2

# print("after deleting d2: ", d1)

# del d1

# print(d1)


# value = "global"

# def level_one():
#     value = "enclosing"
#     def level_two():
#         print(value) # enclosing
#     level_two()

# level_one()
# print(value) # global

# number = 20

# def counter_function():
#     global number
#     number +=1

# counter_function()
# print(f"First call: {number}")
# counter_function()
# print(f"second call {number}")


# def outer_function():
#     message = "Hello! How are you"
#     print(message)
#     def inner_function():
#         nonlocal  message
#         message = "Hello! Hope you are well"

#     inner_function()
#     print(message)
# outer_function()

# import copy
# original = {"scores": [10, 20, 30], "name": "test"}

# shallow = original.copy()
# print(shallow) # {'scores': [10, 20, 30], 'name': 'test'}

# deep = copy.deepcopy(original)
# print(deep) # {'scores': [10, 20, 30], 'name': 'test'}

# shallow['scores'].append(40)
# print(original) # {'scores': [10, 20, 30, 40], 'name': 'test'}
# shallow['name'] = "Changed"
# print(original) # {'scores': [10, 20, 30, 40], 'name': 'test'}
# print(shallow) # {'scores': [10, 20, 30, 40], 'name': 'Changed'}
# deep['scores'].append(50)
# print(original) # {'scores': [10, 20, 30, 40], 'name': 'test'}
# print(deep) # {'scores': [10, 20, 30, 50], 'name': 'test'}

# print(original["scores"] is shallow["scores"]) # True
# print(original["scores"] is deep["scores"]) # False


# def evens(limit):
#     even = 2 
#     while even <= limit:
#         if even %2 == 0:
#             yield even
#         even +=1


# l = evens(6)

# print(next(l)) # 2
# print(next(l)) # 4
# print(next(l)) # 6
# # print(next(l)) # StopIteration

# def noisy():
#     print("starting")
#     yield 1
#     print("middle")
#     yield 2
#     print("end")

# created = noisy()
# print(created) # print object address
# print(next(created)) # 1 starting
# print(next(created)) # 2 middle
# # end doesnt appear because onething is loaded at a time

# def make_multiplier(factor):
#     def multiply(x):
#         return factor * x
#     return multiply

# double = make_multiplier(2)
# triple = make_multiplier(3)

# print(double(5))
# print(triple(5))


# def make_counter():
#     count = 0
#     def increment():
#         nonlocal count
#         count += 1
#         return count
#     return increment

# counter1 = make_counter()
# counter2 = make_counter()

# print(counter1()) # 1
# print(counter1()) # 2
# print(counter1()) # 3
# print(counter2()) # 1

# print(double is triple) # False

from functools import wraps
def shout(upper):
    @wraps(upper)
    def wrapper(*args,**kwags):
       upper_case =  upper(*args,**kwags)
       return upper_case.upper()
    return wrapper


# @shout
# def greet():
#     return "hello there"

# g = greet()
# print(greet.__name__) # wrapper
# print(g) # HELLO THERE


# def greet():
#     return "hello there"

# greet = shout(greet)
# g = greet()
# print(greet.__name__) # wrapper
# print(g) # HELLO THERE


def describe(*args,**kwags):
    print(args,kwags)

describe(1,2,3) #(1,2,3) {}
describe(name="Ali",age = 25) #() {"name":'Ali', "Age": 25}
describe(1,2, name ="Ali")    #(1,2) {"name":'Ali'}

# @shout
# def greet(name):
#     return f"hello {name}"

# print(greet("Ali")) this one fails because there are no arguments in the shout function

# @shout
# def greet(name):
#     return f"hello {name}"

# print(greet("Ali"))

#after adding args and kwags to the decorator I get HELLO ALI

# @shout
# def greet(name):
#     """Returns a greeting for the given name."""
#     return f"hello {name}"

# g = greet("Ali")
# print(g)
# print(greet.__name__) # at first I get wrapper then after changes I get greet
# print(greet.__doc__) # at first Iget none then after changes I get Returns a greeting for the given name.


class Car:
    wheels  = 4
    def __init__(self,make,model):
        self.make = make
        self.model = model
    def __str__(self):
        return f"{self.make} {self.model}"
    def __repr__(self):
        return f"Car(make='{self.make}', model='{self.model}')"
    


car1  = Car("Toyota", "Harrier")
car2 = Car("Nissan", "X-trail")

print(car1.wheels, car2.wheels) # 4
Car.wheels = 6
print(car1.wheels, car2.wheels) #6
car1.wheels = 8
print(car1.wheels, car2.wheels) # 8, 4

print(car1) # toyota harrier
print(str(car1)) # toyota harrier
print(repr(car1)) # Car(make='Toyota', model='Harrier')










