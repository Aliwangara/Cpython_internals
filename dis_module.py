import dis

def module_example():
    x = 10
    y=20

    return x  + y


dis.dis((module_example))