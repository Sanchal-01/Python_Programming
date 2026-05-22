# MAGIC/DUNDER METHODS:

# The magic also called dunder(double underscore) methods are special methods having double underscore at the start and end of their name (eg., __init__, __str__, __len__). 
# These methods allow us to define how our objects interact with built-in python operators,functions and language constructs.
# They provide a way to implement operator overloading and customize the behaviour of our class in a Pythonic way.

# They are used to :
 
# Customize object creation and initialization (__init__ ,__new__ ).
# Enable operator overloading (e.g., + , - ,* ,  == , < ,> ).


#===============================================================================================================================================================================

# NOTE : WHEN TO USE @staticmethod?  Use staticmethod when: method does NOT need self or object data
# Example:

class Math:

    @staticmethod
    def add(a, b):

        return a + b
    
Math.add(2, 3)

#===============================================================================================================================================================================

# 1. __init__ : Object Initialization

# The __init__ method is the constructor. It’s called automatically when a new instance of a class is created. It’s used to initialize the object’s attributes.

class car:
    def __init__(self, model, cost):
        self.model = model
        self.cost = cost

    def car_description(self, type):
        self.type = type
        return(f"The name of the car is {self.model}, costing {self.cost} of type {self.type}.")
    
#     # class Math:

#     @staticmethod
#     def add(a, b):

#         print(a + b)
    
# car.add(2, 3)
 
# print("\n")


b = car("BMW", 100000) 
print(b.car_description("Sedan"))



# 2.__str__ and __repr__ :  String Representation

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return (f"Person({self.name}, {self.age})")  # User-friendly

    def __repr__(self):
        return (f"Person(name='{self.name}', age={self.age})")             # Unambiguous or straightforward for debugging

p = Person("Alice", 30)

print(str(p))    # Person(Alice, 30)

print(repr(p))   # Person(name='Alice', age=30)

print(p)         # Person(Alice, 30)  # print() uses __str__ if available



#3. __len__ – Define Behavior for len()

class Book:
    def __init__(self, title, pages):
        self.title = title
        self.pages = pages

    def __len__(self):
        return self.pages

b = Book("Python 101", 250)
print(len(b))  




# 4. __add__, __sub__, __mul__, etc. – Operator Overloading
# This method allows objects of your class to work with the built-in len() function. It should return the “length” of the object (however you define that).

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)
    
    def __mul__(self, scalar):
      return Vector(self.x * scalar, self.y * scalar)

    def __str__(self):
        return f"Vector({self.x}, {self.y})"

v1 = Vector(2, 3)
v2 = Vector(4, 5)

v3 = v1 + v2   # Calls __add__

print(v3)      # Vector(6, 8)

v4 = v3 - v1
print(v4)      # Vector(4, 5)

v5 = v1 * 5
print(v5)      # Vector(10, 15)












