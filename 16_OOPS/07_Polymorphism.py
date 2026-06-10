# Definition: Polymorphism means "many forms".
# In OOP, polymorphism allows different classes to use the same method name but provide their own implementation.

# Same method name -----> Different behavior

# Poly = Many
# Morph = Forms

class Father:
    def marraige(self):
        return("Marry to Anisha")


class Son(Father):
    def marraige(self):
        return("Marry to Sam")


s = Son()
print(s.marraige())

# ----------------------------------------------------------------------------------#---------------------------------

# TASK : Polymorphism Example

class Car:
    def __init__(self, name):
        self.name = name

    def drive(self):
        print(f"I am driving a {self.name}.")


class Bike:
    def __init__(self, name):
        self.name = name

    def drive(self):
        print(f"I am driving a bike {self.name}.")


class Cycle:
    def __init__(self, name):
        self.name = name

    def drive(self):
        print(f"I am driving a {self.name} cycle.")


# Creating Objects
gaadi = Car("BMW")
motorcycle = Bike("Kawasaki_Ninja_H2R")
bicycle = Cycle("HERO")


# Calling the same method on different objects
gaadi.drive()
motorcycle.drive()
bicycle.drive()
