# CLASS & OBJECT : A class is like a blank form (blueprint). An object is like a filled form with actual data.


# CLASS:
# ----------------------------------------
# A class is a blueprint or template.
# It defines:
# - What data an object will have (variables)
# - What actions it can perform (methods/functions)
# - It does not create the object itself, just the instructions for creating it.
# - It's like an architectural plan for a house.

# Example: "Car" is a class → many cars can be created from it



# OBJECT (Instance):
# ----------------------------------------
# An object is a real instance created from a class.
# Each object has its own unique set of data. 
# It's like the actual house built from the architectural plan.

# Example:
# Car class → BMW,Honda City → these are objects


# NOTE:
# Object = real entity. It is the "thing" in memory.
# Instance = Emphasizes the relationship between the object and its blueprint (the class).
# Analogy: If Car is a blueprint, every car built from it is an object. 
#          A specific red car sitting in your driveway is an instance of that blueprint.



# ----------------------------------------
# CLASS DEFINITION
# ----------------------------------------

class Employee:
    
    # Class Variable (shared by all objects)
    company = "Samsung"
    
    # Method (function inside a class)
    def get_salary(self):
        # 'self' refers to the current object
        # It is automatically passed when a method is called
        
        print("This is object:", self)   # shows memory address of object
        return 120000
    
    def get_salary_1(self):
        return(200000)

# OBJECT CREATION
# ---------------------------
e = Employee()   # object 1
e1 = Employee()  # object 2


# METHOD CALLING : Calling method using object
# --------------------------------------------
print(e.get_salary())   # for object e
print(e1.get_salary_1())  # for object e1


# ACCESSING CLASS VARIABLES
# -------------------------------------------
# Both objects share the same class variable
print(e.company)
print(e1.company)


# ----------------------------------------------
# EXTRA (IMPORTANT )
# ----------------------------------------------

# You can also create object-specific variables
e.name = "Sanchal"
e1.name = "Rahul"

print(e.name)
print(e1.name)

# These values belong only to their respective objects