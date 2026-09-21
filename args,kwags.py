def describe(*args, **kwargs):
    print("args:", args)
    print("kwargs:", kwargs)

describe(1, 2, 3)
describe(name="Ali", age=25)
describe(1, 2, name="Ali")

print("---")

# Why this matters for decorators
def shout(func):
    def wrapper(*args,**kwags):
        result = func(*args,**kwags)
        return result.upper()
    return wrapper

@shout
def greet(name):
    return f"hello {name}"

print(greet("Ali"))   # this will error because greet is using the decorator shoult which doesnt have any argument
# so we need to add args and kwags to wrapper and func for them to accept arguments