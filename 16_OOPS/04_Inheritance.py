# TOPIC : INHERITANCE
# Inheritance means one class can use the traits (attributes and methods) of another class.

# Real life example:
# A child inherits qualities from parents.
# Similarly, a child class inherits features from the parent class.

# ---------------------------------------------------------
# Parent Class = Existing class
# Child Class  = New class using parent class features
# ---------------------------------------------------------


# PARENT CLASS
class Animal:
    # Class Attribute : Shared by all objects created from this class
    Location = "Africa"

    # This is the Constructor of our Parent Class
    def __init__(self, name):

        # Instance Attribute : Value will be different for every object which I assign during the object creation.
        self.name = name


    # Parent Class Method
    def speak(self):
        print("Generic animal sound")


# a = Animal("Bruno")        # Output : Generic animal sound
# a.speak()



# CHILD CLASS : Lion class is inheriting Animal class.

# Meaning: Lion class can use:
# 1. __init__()
# 2. speak()
# 3. Location

# from Animal class automatically.

class Lion(Animal):

    # METHOD OVERRIDING
    # Child class creates its own version of speak()

    def speak(self):

        # super() means: "Go to parent class"
        # Calling parent class speak() method
        super().speak()

        # Additional behavior of Lion
        print("Roarrrrrrrr....!!")



# OBJECT OF PARENT CLASS
#----------------------------------------------------------------------------------------
a = Animal("Tiger")  # self.name = "Tiger"

print(a.name)
a.speak()           # Calling parent class method
print(a.Location)   # Accessing class attribute
 
print("\n")



# OBJECT OF CHILD CLASS
#-----------------------------------------------------------------------------------------

# Lion class does NOT have its own constructor. 
# So it automatically uses Animal class constructor.

b = Lion("Simba")  # Internally: Animal.__init__(b, "Simba")
print(b.name)
b.speak() # Calling overridden method

# Child class also inherited class attribute
print(b.Location)

#----------------------------------------------------------------------------------------

# IMPORTANT NOTE:

# 1. Child class automatically gets access to parent class methods and attributes.
# 2. super() is used to access parent class things.
# 3. Method overriding means: Child class changes the behavior of parent class method.
# 4. Inheritance helps in:
#    - code reusability
#    - less repetition
#    - cleaner programs

#----------------------------------------------------------------------------------------

# OUTPUT UNDERSTANDING

# a.speak()
# OUTPUT:Generic animal sound

# b.speak()
# OUTPUT: Generic animal sound, Roarrrrr!

# Why both?
# Because: super().speak() runs parent method first then child method runs.