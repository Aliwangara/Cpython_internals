import dis

def check(n):
    if n > 10:
        return "big"
    else:
        return "small"



# dis.dis(check)

a = 1000
b = 1000
c = a

print(a is b)
print(id(a), id(b))
print(a is c)
print(a == b)

