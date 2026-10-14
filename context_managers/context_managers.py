from contextlib import contextmanager


# with open('context_managers/first_t.txt','w') as f:
#     f.write("Hello lorem ipsum")


# class OpenFile:
#     def __init__(self,file_name,mode,):
#         self.file_name = file_name
#         self.mode = mode
        

#     def __enter__(self):
#         self.file = open(self.file_name,self.mode)
#         return self.file
#     def __exit__(self, exc_type, exc_val, traceback):
#         self.file.close()

# with OpenFile("context_managers/first_t.txt",'w') as f:
#     f.write("Testing")

# print(f.closed)


# context manager using functions

@contextmanager
def open_file(file_name,mode):
    f = open(file_name,mode)
    yield f
    f.close()

with open('context_managers/first_t.txt','w') as f:
    f.write("Hello guys Lorem Ipsum")

print(f.closed)


class Demo:
    def __enter__(self):
        print("entering")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("exiting")
        return True

with Demo() as d:
    print("inside the block")

print("---")

# What if something goes wrong inside the block?
try:
    with Demo() as d:
        print("about to fail")
        raise ValueError("oops")
        print("this line never runs")
except ValueError:
    print("caught the error outside")

print("---")

# A real one you already use
with open("test.txt", "w") as f:
    f.write("hello")
print(f.closed)    # what does this print, and why?