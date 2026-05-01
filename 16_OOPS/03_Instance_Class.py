# If we have a class in python, there can be :
# - object(instance) attributes &
# - class attributes
# NOTE : The instance attribute is specific to an instance and the class attribute is specific to a class.


class vehicle:
    vehicle_type ="SUV- Sub Utility Vehicle"

    def __init__(self, name, cost, vehicle_type):
        self.name = name   
        self.cost = cost                   # Create an instance attribute named cost
        self.vehicle_type = vehicle_type

c = vehicle("BMW", 20000000, "Sedan")
print(c.vehicle_type)        # This will always print the instance attribute whenever present.

# c = vehicle("BMW", 20000000)
# print(c.vehicle_type)

print(vehicle.vehicle_type)   
# This will always print the class attribute.
# So if we want to print the name of class attribute we need to use the name of class followed by class attribute/variable.

# Object Introspection
print(dir(c))