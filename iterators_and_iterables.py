# Iterable - something that can be looped over eg: list

# if soemthng is iterable then it needs to have a special method __iter__()

nums = [1,2,3,4]
# to looks at methods and attributes available to a specic object we use the dir eg:
print(dir(nums))

# iterator - is an object with state which knows where it is during iteration. we can say
#  a list doesnt know where to get next value

class Countdown:
    def __init__(self, start):
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= 0:
            raise StopIteration
        value = self.current
        self.current -= 1
        return value

for n in Countdown(3):
    print(n) # 3 2 1 

print("---") # ---

it = Countdown(2)
print(next(it)) # 2
print(next(it)) # 1
try:
    print(next(it)) # Raises the print StopIteration
except StopIteration:
    print("StopIteration")

print("---") # ---

c = Countdown(3)
print(list(c)) # [3,2,1]
print(list(c)) # []
