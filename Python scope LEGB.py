""""
LEGB
local - Variables stored inside a function
enclosing - variables within a local scope of an enclosing function(Dont seem to understand though)
Global - are variable that can be accesses within the code and its declared at the top of a module or its explicitly declared with Global
Build-in - names pre assigned in python


when a code runs it starts by checking variables in the order of LEGB first checks if there is a local variable,enclosing,global and built in
"""

# Global and local variable

x = "Global x"
# this is a global variable because its inside the document but not controlled by a scope or anything it can be accesses anywhere within the file

def test():

    x = "local x"
    print(x) # this prints local X
test()
print(x) # this prints global x

# X inside the function cant be printed outside the function because function limits its coverage
#  global X can even be used inside the function eg:

def global_var():
    print(x) # this prints Global x
global_var()

# or another way to access the variable we use

def g_var():
    global X # using the global tag to now make the variable inside a function to be used outside the function

    X = "G_variable"
g_var()
print(X) # here I get g_var because I have made it accessible outside its scope


# built-in are variables that are already predefined by python and perform certain operations eg:

x = min([1,2,5,3]) # min is a built in var
print(x)

import builtins 
# print(dir(builtins)) # used to check types of variables inside the builtin function

# built in can be overwritten if you name a variable or function same as iit

def min():
    pass
min()

# z = min([1,2,5,3])

#  the mean at the top will be shown but the one with z variable will display
#  an error because of the function that has taken up its name and overwritten it


## enclosing - This deals with nested functions ( a function within a function) eg:

# def outer():
#     b = "outer scope" # local to outer function

#     def inner():
#         b = "inner scope" # local to inner function
#         print(b)
#     inner()
#     print(b)
# outer()
#  these two prints outer and inner but:

def outer():
    b = "outer scope"

    def inner():
        b = "inner scope"
        print(b)
    inner()
    print(b)
outer()

# this prints 'outer scope' and 'outer scope' because the function first checks if there is x in the local inner function
# doesnt find it so it proceeds to the enclosing local function which is outer scope and finds x then prints
# thats enclosing. if:

# def outer():
#     b = "outer scope" # if I comment out this then print:

#     def inner():
#         # b = "inner scope"
#         print(b)
#     inner()
#     print(b)
# outer()

# if I comment out b on the outer scope then try printing I will get an error because the inner scope finds
# a local variable inside the inner scope but now the second print inside the outer scope tries checking 
# if there is b variable in the local function doesnt find then it moves to the global area to check if 
# there is a global variable it doesnt find so throws the error
#Inside the inner function I can use the non local statement to make values in the enclosing function perform what 
#values inside the secodn function satets EG:

def outer_scope():
    g = "outer g"

    def inner_scope():
        nonlocal g
        g = "inner g"
        print(g)
    inner_scope()
    print(g)
outer_scope()

# this prints inner g


count = 0

def increment():
    count += 1
    print(count)

increment()