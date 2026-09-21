# Closures are Python's other way of having a function "remember" 
# something between calls, without generators. 
'''
or we can say closure are variables preserved by the outer function when it runs to be used by the inner functions
'''

# I have just memorised the syntax I saw on the youtube video this topic is kindoff shacky for me
# def outer_func():
#     message = 'HI'
    
#     def inner_func():
#         print(message)
        

#     return inner_func
    

# msg_func = outer_func()
# msg_func()

# using parameters I can do

def outer_func(msg):
    message = msg

    def inner_func():
        print(message) # free variable

    return inner_func

# from here I was kinda confused 
hi_func = outer_func("hi")
hello_func = outer_func("hello")

hi_func()
hello_func()


        