# functools help decorators to behave like original function from the outside

from functools import wraps

def shout(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result.upper()
    return wrapper

@shout
def greet(name):
    """Returns a greeting."""
    return f"hello {name}"

print(greet.__name__)   # wrapper
print(greet.__doc__)    # the docstring — what happens to it? not sure

print("---")

# Now the fix
def shout_fixed(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result.upper()
    return wrapper

@shout_fixed
def greet2(name):
    """Returns a greeting."""
    return f"hello {name}"

print(greet2.__name__)
print(greet2.__doc__)