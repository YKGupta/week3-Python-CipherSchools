# Eager Loading
# First generate all the values then return them 
def fun(n):
    return [ i**2 for i in range(1, n) ]

# Ohkk
for i in fun(8):
    print(i, end = " ")
print()

print("-"*21)

# But :o
# for i in fun(1000000000000000):     # This is going to be static(no output) for sometime since it will first generate the list completely then the iteration would start
    # print(i, end = " ")

# To avoid the above, we use Lazy Loading ie generating values on the fly :)
def fun(n):
    for i in range(1, n):
        yield i**2
# for i in fun(1000000000000000):     # This will keep on printing as well as generating
    # print(i, end = " ")

# 'yield' keyword
# The yield keyword is used to transfer the control to the parent
# ie it generates the result, then pauses the execution of that(say function) and transfers the control to the 
# call statement and then we can use that value and then when the next iteration is called then the next 
# iteration of the function would done(ie resumed).

# Example
def fun():
    print("Started")
    yield 1
    print("Yielded 1")
    yield 2
    print("Yielded 2")

it = iter(fun())
next(it)
print("Phewwwww... that was long, let's continue :)...")
next(it)
print("Hmm... going good :)...")
try:
    next(it)
except StopIteration as e:
    print("Stop iteration exception was raised")

print("-"*21)

from time import sleep
def fun():
    print("Started")
    yield
    sleep(5)
    print("Ended")

it = iter(fun())
next(it)
print("You know what? An iteration just finished :)")
try:
    next(it)
except StopIteration as e:
    print("Stop iteration exception was raised")

print("-"*21)

# Note- 'yield' keyword if present in the body of a function, then it returns a 'generator'

# Generators are basically iterators, ie we can call the '__next__' method on them directly
# If you try to fetch the 'iterator' of the generator by '__iter__', then it would return the same generator object

# Generators can be created by using '()'
a = ( i**2 for i in range(10) )
print(type(a), a)              # Generator object
print(type(iter(a)), a)        # Same generator object (ie memory address as well)
for i in a:
    print(i, end = " ")