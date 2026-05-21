# Instance Methods :
# =============================================================================================================================================================
# These are the most common type of method. They operate on instances of the class (Object) and have access to the instance's data through the self parameter.

class Employee:
    company = "Dream121"
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary


    def print_info(self):
        print(f"The name is {self.name} and the salary is {self.salary}.")
    
e1 = Employee("Sanju",10345)
e2 = Employee("Samson", 12345)

print(Employee.company)      # Dream121

# print(Employee.name)       # This will throw an error as we name is not the class attribute instead its an instance attribute.

e1.print_info()
e2.print_info()

# By default a method inside a class is an instance method.




# STATIC METHODS :
# ===========================================================================================================================
# These methods are associated with the class, but they don't have access to either the instance (self) or the class (cls).
# They are essentially regular functions that are logically grouped within a class for organizational purposes.


class Employee:
    company = "Dream121"
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary


    def print_info(self):
        print(f"The name is {self.name} and the salary is {self.salary}.")

    @staticmethod
    def sum(a,b):
        return(f"The sum of two number is {a+b}.")
    
e1 = Employee("Sanju",10345)

# print(e2.sum(5, 20))  # Type Error :Employee.sum() takes 2 positional arguments but 3 were given. 2 arguments = a and b.  The third argument was self automatically passed.

# Now we use static method : Static methods doesn't use the instance attribute or the instance of the object on which they are being called.
# In this case we are using e2 and we don't need to know what e2 is, what the name in e2 is what the salary of e2 is, etc.
print(e1.sum(5, 20)) 



# CLASS METHOD :
# =======================================================================================================================================================================
# These methods are bound to the class itself, not to any particular instance. They have access to class- level attributes and can be used to modify the class state. 
# They receive the class itself (conventionally named cls) as the first argument.


class Employee1:
    company = "Lenovo"
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary


    def print_info(self):
        print(f"The name is {self.name} and the salary is {self.salary}.")

    @staticmethod
    def sum(a,b):
        return(f"The sum of two number is {a+b}.")
    
    # Class Methods
    @classmethod
    def print_company(cls):
        print(cls.company)

    @classmethod
    def change_company(cls, new_company):
        cls.company = new_company


Emp1 = Employee1("Sanchal", 1200000)
print(Emp1.company)
Emp1.change_company("Acer")
print(f"The new changed company would be {Emp1.company}")