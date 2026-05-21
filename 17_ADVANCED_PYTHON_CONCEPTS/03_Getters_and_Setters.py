# =========================================================
# TOPIC : GETTERS & SETTERS IN PYTHON
# =========================================================

# In object-oriented programming, getters and setters are methods used to control access to an object’s attributes (also known as properties or instance variables).
# They provide a way to encapsulate the internal representation of an object, allowing you to validate data, enforce constraints, and perform other operations when an attribute is accessed or modified. 
# While Python doesn’t have private variables in the same way as languages like Java, the convention is to use a leading underscore ( _ ) to indicate that an attribute is intended for internal use.



# Getters and Setters are used to:
# 1. Control access to object attributes.
# 2. Validate data.
# 3. Modify behavior during getting/setting values.
# 4. Achieve encapsulation.

# Encapsulation means:
# Hiding internal implementation details and controlling how data is accessed or modified.



# BASIC CLASS EXAMPLE
# =========================================================

class Employee:
    def __init__(self, name, salary):
        self.name =name
        self.salary = salary

e = Employee("Jack Sparrow", 1000000)
print(e.name, e.salary)



# TRADITIONAL GETTERS & SETTERS
# =========================================================

# In traditional approach,
# we create separate methods for:
# 1. Getting values
# 2. Setting/modifying values

class Person:
    def __init__(self, name):
        self._name = name        # Convention: underscore (_) denotes "This attribute is intended for internal use."  It is NOT truly private.


    # GETTER METHOD: Used to access values
    def get_name(self):
        return self._name


    # SETTER METHOD: Used to modify values
    def set_name(self, new_name):
        self._name = new_name 

p = Person("Alice")
print(p.get_name())   # Calling Getter  # Alice

p.set_name("Bob")     # Calling Setter
print(p.get_name())   # Bob 



# IMPORTANT NOTE:
# Python does NOT strictly prevent access.

# We can still directly access:
p._name = "Bob"
print(p._name)     # Bob 





# USING @property DECORATOR
# =========================================================
# Python provides a more elegant and concise way to implement getters and setters using the @ property decorator.
# This allows us to access and modify attributes using the usual dot notation(e.g. p.name) while still having the benefits of getter and setter.




class Person:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):  # Getter
        return self._name

    @name.setter
    def name(self, new_name):  # Setter
        self._name = new_name 

p = Person("Alice")
print(p.name)  # Alice (calls the getter)

p.name = "Bob"  # Calls the setter
print(p.name)  # Bob





# EXAMPLE 3: REAL LIFE ONE

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        

    @property 
    def first_name(self):
        l = self.name.split(" ")   # this is the split before and after the space between the First and Last name.
        return l [0]
    
    @ first_name.setter
    def first_name(self, first):
        l = self.name.split(" ")
        new_name = f"{first} {l[1]}"
        self.name = new_name
    
f = Employee("Jack Sparrow", 100000)
print(f.first_name)     # Jack

# Calls getter internally : Looks like property access but actually getter method runs internally
print(f.first_name)    # f.first_name is a function but it looks like a property because we are using property decorator.

# Calls setter internally
f.first_name = "Sanchal"

# Full name updated
print(f.name)



# FINAL DEFINITION

# Getters and Setters are methods used to control how object attributes are accessed and modified.
# Python provides a clean way to implement them using @property and @property_name.setter decorators.