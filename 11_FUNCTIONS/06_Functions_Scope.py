# In Python, variables have scope (where they can be accessed easily) and lifetime (how long they can exist). 
# Variables are created when a function is called and destroyed when it returns.
# Understanding scope improves our code organization.

# TYPES of SCOPES:
# - Local Scope (inside a function) 
# - Global Scope (accessible everywhere) 

z = 5    # GLOBAL SCOPE Variable   


#1 Local Scope
def sum(a, b):    
    c = a + b        # a & b are called local variable i.e., These variables can be accessed inside a function only not outside it.
    z = 1         # This creates a local variable called z which is destroyed after this function returns.
    return (c)
   
print(sum(2, 5))


def greet():
    z = 24            # z is a local variable here.
    print("Hello/Hey!!")
greet()


# print(c)  # NOTE: Not allowed as value of c is unknown/ not assigned

# When we write 4, 6 --> 4 and 6 are passed as a & b to this function. 
# The moment we pass 4 and 6 to a & b, a is 4 and b is 6 and c becomes 10, now once c becomes 10 what will happen is it will be returned and once it is returned value of a, b and c will be wiped out of the memory, and that's how functions work in python.



#2 Global Scope:

def hello():           # z is a global variable, since it is declared outside a function and z=5 at line (9).
    print (z)
hello()





