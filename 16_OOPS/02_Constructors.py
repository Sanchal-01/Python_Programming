# CONSTRUCTORS 
# A constructor is a special method in a class that is automatically called when an object is created and is used to initialize the object’s attributes.

class Employee:

    def __init__(self, salary, name, bond):
        # Constructor automatically runs when object is created
        self.salary = salary
        self.name = name
        self.bond = bond

    def get_salary(self):
        return self.salary


# Object creation → __init__ runs here automatically
e = Employee(12400, "Robin", 3)
e1 = Employee(20000, "Sanchal", 1)

# Correct usage → access attributes
print(e.name)
print(e.salary)
print(e.bond)

# Call method
print(f"The monthly salary is {e1.get_salary()}")

print(("\n"))

#-----------------------#----------------------#------------------#------------------#--------------------#------------------#---------------------#----------------------#-------------------#----------------------#


class Dog:
    def __init__(self, name, breed):     # The constructor
        self.name = name                       # Setting the name attribute
        self.breed = breed                     # Setting the breed attribute

# When we do this:
my_dog = Dog("Fido", "Poodle")  # The __init__ method is automatically called
print(my_dog.name,my_dog.breed)

# It's like we're saying:
# 1. Create a new Dog object.
# 2. Run the __init__ method on this new object:
#    - Set my_dog.name to "Fido"
#    - Set my_dog.breed to "Poodle"

print(("\n"))


class Dog:
    def __init__(self, name="Unknown", breed="Mixed"):
        self.name = name
        self.breed = breed

dog1 = Dog()          # name will be "Unknown", breed will be "Mixed"
dog2 = Dog("Rexi")     # name will be "Rex", breed will be "Mixed"
dog3 = Dog("Bella", "Labrador") # name will be "Bella", breed will be "Labrador"
print(dog2.name,dog2.breed)

print("\n")

#-----------------------#----------------------#------------------#------------------#--------------------#------------------#---------------------#----------------------#-------------------#----------------------#


# Simple rule yaad rakhna :

# ❌ __init__() ko manually call mat karna. __init__() kuch return nahi karta, return value = None
# ✅ Object bana → data use kar like e.(data)

# The constructor (__init__) is not meant to be called directly. 
# It runs automatically when an object is created and is used to initialize the object’s attributes.
# Constructor = automatic setup of object data.



# Ye Example maine khudse  try kiya : Correct in 1st time 

class Student:

    def __init__(self, name, standard, rank):   # yaha maine constructor ko instance attributes assign kiyen
        self.name = name
        self.standard = standard
        self.rank = rank
    
    def student_info(self):
        return(f"The name is {self.name} studying in standard {self.standard} holding a rank of {self.rank} in the class.")


s = Student("Sanchal", " 6th Sem", "TOP 5")
print(s.student_info()) 
        


