# Docstrings are used to document functions, classes, and modules. In Python, they are written in triple quotes.
# They are accessible using the __doc__ attribute. 
# Doc attribute helps make our code more readable.

def add(a, b):
    """Returns the sum of two numbers."""
    return a + b

print(add.__doc__)   # Output: Returns the sum of two numbers.     
   
print("-" *50,"\n ")


def add(a, b):
    """
        Parameters:
        a (int): The first number.
        b (int): The second number.
        
        Returns:
        int: The sum of the two numbers.
        """
    return a + b

print(add.__doc__)