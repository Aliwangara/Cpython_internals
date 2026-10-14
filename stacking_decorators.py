# more than one decorator can be placed ontop of a function that is what we call chaining / stacking decorators



import functools

def square_brackets(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        return f"[{func(*args, **kwargs)}]"
    return wrapper

def angle_brackets(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        return f"<{func(*args, **kwargs)}>"
    return wrapper

@square_brackets
@angle_brackets
def greet(name):
    return f"hello {name}"

print(greet("Ali")) # this will run square barcket then angle bracket puts square bracket at the outermost part

print("---")

@angle_brackets
@square_brackets
def greet2(name):
    return f"hello {name}"

# greet2 = angle_brackets(square_brackets(greet2)) we can also chain it this wasy

print(greet2("Ali")) # this will run  angle bracket and then run square brackets gives the output with angle brackets at the outermost part