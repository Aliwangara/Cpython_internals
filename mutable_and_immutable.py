# Mutable are objects whose states can be changes
# immutable are objects whose state cant be changed after creating

#things that are immutable: Strings eg:

a = "wangara"
print(a)
# a = "Ali"
# print(a)
# These two will work because its like I have assigned two different values to different variables although they share names

# a[0] = "W"
# print(a)

# I get an error because strings are not mutable 

# Ints are immutable too eg:
def try_change(n):
    n += 1

x = 5
try_change(x)
print(x)  # still 5

# Mutable example is a list

list_a  = [1,2,3,4,5]
print((id(list_a)))

list_a[0] = 8

print(id(list_a))

# the list changes to [8, 2, 3, 4, 5] meaning it can be changed after creation


# immutable objects passed into functions can't be changed in place, so the function operates 
# on a copy-like new value; mutable objects passed into functions share the same underlying object, 
# so changes inside the function are visible outside it too.
