def outer_function(func):
    def wrapper():
        print("wrapped!")
        func()
    return wrapper

def display():
    print("original display")

my_func = outer_function(display)

display()    # what does this print?
my_func()    # what does this print?