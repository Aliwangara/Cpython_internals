import sys

a = [1, 2, 3]
print(sys.getrefcount(a))   # expect 2 (1 real + 1 from the function call itself)

b = a
print(sys.getrefcount(a))   # expect 3 (2 real + 1 from the function call)

del b
print(sys.getrefcount(a))   # expect 2 (back to 1 real + 1 from the call)