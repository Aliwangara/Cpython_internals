# A generator is better than a list when you look at it interms of perfomance and memory

# def square_numbers(numb):
#     results = []

#     for i in numb:
#         results.append(i*i)
#     return results

# my_nums = square_numbers([1,2,3,4])
# print(my_nums) # [1, 4, 9, 16]

'''
This is the process of now converting to a generator
'''


# def square_numbers(numb):
#     for i in numb:
#         yield (i*i)
    

# my_nums = square_numbers([1,2,3,4])
# print(my_nums) # I get a generator <generator object square_numbers at 0x000001A09857B5E0>

def square_numbers(numb):
    for i in numb:
        yield (i*i)

my_nums = square_numbers([1,2,3,4])

# print(next(my_nums))  1
# print(next(my_nums))  4
# print(next(my_nums))   9
# print(next(my_nums))   16  
# print(next(my_nums)) throws an error because iteration has reached the end

# we can use for loop for the generators  eg:
# for num in my_nums:
#     print(num) 1,4,16,9

'''
we can use list comprehension incase we dont want a whole function

'''

my_numbers = [x*x for x in [1,2,3,4,5]]

# we can convert this to generator by using parenthesis eg:

# my_numbers = (x*x for x in [1,2,3,4,5])
# print(my_numbers)  <generator object <genexpr> at 0x00000290321BA4D0>
# we can check the numbers or figures by doing
# print(list(my_numbers))  [1, 4, 9, 16, 25] when you convert a generator to a list we loose advantages we had with 
# generators interms of performance



for number in my_numbers:
    print(number)



# Part 1 — the iterator protocol
my_list = [1, 2, 3]
my_iter = iter(my_list)      # this is what GET_ITER does

print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
# print(next(my_iter))   # StopIteration error

print("---")

# Part 2 — a generator
def count_up_to(n):
    i = 1
    while i <= n:
        yield i
        i += 1

gen = count_up_to(3)
print(gen)              # what does this print? not what you'd expect
print(next(gen))
print(next(gen))
print(next(gen))
# print(next(gen))        # StopIteration

print("---")

# Part 3 — generators are lazy
def noisy_gen():
    print("starting")
    yield 1
    print("middle")
    yield 2
    print("end")

g = noisy_gen()
print("created generator, nothing printed yet") 
print(next(g))
print(next(g))



