# python interpreter has values stored from -5 to 256 so when you create an object with a value of 20 
# its inside the values -5 to 256. anything above that eg 300 is out of the scope



a = 20
c= a
print(c)
# this prints 20 because the value already exists in the memory

c= 20 +1 
print(c)

# Here the C stops pointing to the value of a and created a new object with the value 21

d = 20

# whenever you create a new variable with a value like above the python checks if the value is in the interpreter memory -5 to 256

# if the variable d later changes maybe to "Ali" since its a foreign word it stores the value to heap memory

# system OS memory allocates some memories to python interpreter which has two kind of memory:
#Stack memory - executes all codes in sequency: functions,class and Heap memory - all memory allocation is done here

# python execution starts from the main method stack memory eg:
a = 10
# Stack memory stores 'a' heap memory stores 10