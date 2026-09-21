'''
in closure the variable needed is preserved by the outer_function for the inner function.
for decorators the preserved now is not a variable its a function which gets called by the inner function
the function can be a parameter eg:
'''

def my_decorator(func):

    def wrapper():
        print("before")
        func()
        print("After")
    return wrapper

# def say_hi():
#     print("hi")

# decorated = my_decorator(say_hi)

# decorated()

'''
instead of this line   decorated = my_decorator(say_hi)
we can use the @ to write decorators eg:

'''
@my_decorator
def say_hi():
    print("hi")

say_hi()


