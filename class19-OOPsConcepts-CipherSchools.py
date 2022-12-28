# Every thing in python is a object
# Be it a class, function, variable, etc.
print(type(int))
# Type is another class which hold all datatypes
print(type(object))
print(isinstance(int, object))
print(isinstance(5, int))
print(isinstance(5, object))
class Demo:
    pass
print(type(Demo))
def fun():
    pass
print(type(fun))
print(isinstance(fun, object))

print("-"*21)

# Callable classes
class A:
    def __call__(self):
        print("Hemlooo")
ob = A()
# Below two are same
ob()
ob.__call__()

print("-"*21)

# Python has dunders for every operation that happens be it a for loop!

# Like you can define a dunder for syntactical operation like index
d = {"name":"Yash Kumar Gupta", "Age":"100"}
print(d["name"], d.__getitem__("name"))     # Both are same

print("-"*21)

#Similarly
class IndexMe:
    def __init__(self, n):
        self.n = n
    
    def __getitem__(self, x):
        return x ** self.n

obj = IndexMe(5)
print(obj[3], obj[2])

print("-"*21)

# Always define immutable members as class variables only!!!!
class Wrong:
    l = []
    def __init__(self, name):
        self.name = name
    
    def add(self, e):
        self.l.append(e)

objj = Wrong("Yash Kumar Gupta")
objj.add(2)
objj.add(5)
objj.add(11)
print(objj.l)
objj2 = Wrong("New Object With Same List :(")
print(objj2.l)
# Hence do not declare mutable members as class variables :)
print("-"*21)