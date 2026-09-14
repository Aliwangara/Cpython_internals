# == used to describe the general or the outlook of two things, two sets of twins each wearing the same clothes
# it like asking do they look same yes(==) but is it the same person NO(because they are two different people) 
# while is checks things like volume etc 
# so basically is checks the background lets say the memory allocation and stuff

l1 = [1,2,3,4,5]
l2 = [1,2,3,4,5]

if l1 is l2:
    print(True)
else:
    print(False)

# this will give out false because it asks do they look the same yes

l3 = [1,2,3,4,5]
l4 = [1,2,3,4,5]

if l3 == l4:
    print(True)
else:
    print(False)

# This prints out True because its like asking is it the same, No

l5 = [1,2,3,4,5]
l6=l5

print(id(l5), id(l6))
print(id(l5) == id(l6))

# This now shows the work is does on the background

