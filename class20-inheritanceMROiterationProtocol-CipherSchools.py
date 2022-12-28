class A:
    def __init__(self):
        print("A's init was executed")

class B(A):
    def __init__(self):
        print("B's init was executed")
        super().__init__()

ob = B()
# Python has no concept of method overloading (Remember!)
# 'super()' = object of parent classes'

print("-"*21)

class A:
    x = 8
    y = 8
class B(A):
    x = 5
class C(B):
    pass
class D(A):
    x = 10
class E(C, D):
    pass

# MRO - Method Resolution Order is the order in which the methods/properties of the classes will be resolved
# There are two rules
#   - DFS
#   - If there is a loop solve branches differently (:) not much idea) (root note iterated at the last)

e = E()
print(E.mro())
print(e.x, e.y)     # x = 5, y = 8 on the basis of the MRO

print("-"*21)

# Iteration Protocol
# For any object to be iterable, it should have two(2) dunders
#   - __iter__
#   - __next__

# Example
a = range(8)
it = a.__iter__()               # or it = iter(a)
print(it.__next__())    # 0     # or print(next(it))
print(it.__next__())    # 1
print(it.__next__())    # 2
print(it.__next__())    # 3
print(it.__next__())    # 4
print(it.__next__())    # 5
print(it.__next__())    # 6
print(it.__next__())    # 7
try:
    print(it.__next__())    # When end encounted -> 'StopIteration' exception raised
except StopIteration as e:
    print("Stop Iteration error encountered")

print("-"*21)

# Protocol
#   - object's '__iter__' method should return an iterator
#   - iterator's '__next__' method should return the new value on every call
#   - if the iterator reaches the end, it should raise an 'StopIteration' exception

# Let's create our own iterable :)
class yashTheIterable:
    def __init__(self, n):
        self.n = n
    
    def __iter__(self):
        return yashTheIterator(self)

class yashTheIterator:
    def __init__(self, yashTheIterableObj):
        self.yashTheIterableObj = yashTheIterableObj
        self.i = 0      # Initial value of the iterator(kind of)

    def __next__(self):
        ret = self.i
        self.i += 1
        
        # Protocol's third step (raising exception)
        if (ret >= self.yashTheIterableObj.n):
            raise StopIteration

        return ret

a = yashTheIterable(8)
it = iter(a)
print(next(it))     # 0
print(next(it))     # 1
print(next(it))     # 2
print(next(it))     # 3
print(next(it))     # 4
print(next(it))     # 5
print(next(it))     # 6
print(next(it))     # 7
try:
    print(next(it))    # When end encounted -> 'StopIteration' exception raised
except StopIteration as e:
    print("Stop Iteration error encountered")

print("-"*21)

# or use it as range's alternative :)
for i in yashTheIterable(8):
    print(i)

print("-"*21)