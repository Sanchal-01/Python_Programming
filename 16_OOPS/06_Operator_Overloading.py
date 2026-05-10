# TOPIC : OPERATOR OVERLOADING IN PYTHON

# Operator Overloading means: Giving special meaning to operators(+, -, *, etc.) for user-defined objects.

# Example: Normally: 2 + 3 = 5

# But for objects: p1 + p2, Python does not know HOW to add two objects.
# So we define that behavior manuallyusing special methods like: __add__() , __sub__() , __mul__()


# NORMAL METHOD APPROACH which I took Initially :

class Point:
        # Constructor
        def __init__(self, x, y): # Instance parameters              
                self.x = x
                self.y = y

        # Normal method for adding two points

        def sum(self, p):  # self --> first object  , p --> second object    
                return Point((self.x + p.x),(self.y + p.y))  # Returning NEW Point object
        
        # Method for displaying point values
        def print_point(self):
             print(f"x is {self.x} and y is {self.y}")


# OBJECT CREATION
p1 = Point(3, 2)
p2 = Point(6, 3)

# Internally: Point.sum(p1, p2), self = p1, p = p2

p = p1.sum(p2)

# New object contains:
# x = 3 + 6 = 9
# y = 2 + 3 = 5

p.print_point()

print("\n")







# METHOD 2: OPERATOR OVERLOADING USING __add__()

class Point:
        # Constructor
        def __init__(self, x, y):
                self.x = x
                self.y = y

        # OPERATOR OVERLOADING :This method runs automatically when + operator is used.
        def __add__(self, p):
                return Point((self.x + p.x),(self.y + p.y)) # Returning new Point object

        # Display method
        def print_point2(self):
                print(f"The value of x is {self.x} and y is {self.y}")


# OBJECTS
p1 = Point(12, 20)
p2 = Point(8, 5)


# Instead of: p1.sum(p2)
# We can now directly write: p1 + p2

# Internally Python converts:

# NOTE: p1 + p2 into ----> p1.__add__(p2)

p = p1 + p2
# Final values: x = 20, y = 25

p.print_point2()


# IMPORTANT THINGS THAT I HAVE UNDERSTOOD AFTER STUDING OPERATOR OVERLOADING:

# 1. __add__()
#    Special method used for + operator.

# 2. self Represents first object.

# 3. p Represents second object.

# 4. return Point(...) Creates and returns a NEW object.

# 5. Operator overloading makes code:
# - cleaner,
# - more readable,
# - closer to real mathematics.