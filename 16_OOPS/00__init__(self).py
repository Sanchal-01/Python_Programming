# self represents:
# The current object (instance) of the class.

# It is used to:
# 1. Access instance attributes
# 2. Differentiate object data
# 3. Connect object data with methods

# Important:
# self is NOT a keyword.
# It is just a naming convention used in Python.



class Car:
    def __init__(self, brand: str, fuel_type: str):
        self.brand = brand
        self.fuel_type = fuel_type
    
    def drive(self, distance: float):
        print(f"Driving {self.brand} for {distance}km on [{self.fuel_type}].")   # The argument without self does not reply on the instance --->its going to take data on spot.


Toyota = Car(brand = "Toyota", fuel_type = "Diesel")
print(Toyota.brand)
Toyota.drive(distance= 40)


Competition3= Car(brand="BMW", fuel_type= "Petrol")
print(Competition3.brand)
Competition3.drive(1000)



# -------------------------------------------------------
# IMPORTANT NOTES
# -------------------------------------------------------

# 1. Every object has its own separate data.

# Example:
# Toyota object stores:
#   brand = Toyota
#   fuel_type = Diesel

# BMW object stores:
#   brand = BMW
#   fuel_type = Petrol


# 2. self helps Python identify: "Which object's data should be used?"

# 3. Internally Python converts: Toyota.drive(40)
# into: Car.drive(Toyota, 40)
# So: self = Toyota object

# 4. Without self: methods cannot access object attributes.

# 5. Instance Attributes: Values different for every object.
# Example:
# self.brand
# self.fuel_type

# 6. Methods: Functions written inside a class.


