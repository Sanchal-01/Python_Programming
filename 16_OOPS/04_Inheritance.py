# TOPIC : INHERITANCE
# Inheritance means one class can use the traits (attributes and methods) of another class.

# Real life example:
# A child inherits qualities from parents.
# Similarly, a child class inherits features from the parent class.


# Parent Class = Existing class
# Child Class  = New class using parent class features.


# Parent Class
class Animal:

    # Constructor
    def __init__(self, name):
        self.name = name

    # Parent class method
    def speak(self):
        print("Generic animal sound")


# Child Class <----- "inheriting" Animal
class Lion(Animal):
    pass


# OBJECT OF CHILD CLASS :

a = Lion("Bruno")
print(a.name)        # Inherited from Animal class
a.speak()            # Inherited method from parent class

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

# Application of Inheritance where ----> Child class has own method

class Lion1(Animal):

    def roar(self):
        print(f"{self.name} says Roarrrrr!")      # {current object.something}


b = Lion1("Mufasa")
b.roar()             # Child class own method

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

# During function call we write {current object.something}, somethong can be as follows:        

# |         Type            |    Example      |
# | ----------------------- | --------------- |
# | 1. Attribute / Variable | object.name     |
# | 2. Method / Function    | object.speak()  |
# | 3. Class Attribute      | object.company  |


#  Inheritance helps in:
#    - code reusability
#    - less repetition
#    - cleaner programs

