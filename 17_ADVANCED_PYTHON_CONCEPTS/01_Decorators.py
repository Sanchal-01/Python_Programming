# Decorators are used when we want to add extra functionality before or after an existing function without modifying it's original code.
# This is often referred to as meta-programming, where one part of the prograam tries to modify another part of the program at compile time.

def say_hello():
    print("Hello!! How are you ?")

say_hello()

print("\n")



# What if we want to use the say_hello() function inside another function, and also execute some code before and after the say_hello() function?
# We might need nested function.

# For this purpose, we use Decorators. Decorators allow us to modify or extend the behavior of a function without changing its original code.


def decorators(function):

    def wrapper():        # This function adds extra behavior.
        
        print(f"This code is  executed before {function.__name__} function.")   # Yaha pe maine function name ko dynamic banaya hai function ke name attribute ko use karke.

        # Calling original function
        function()

        print(f"This code is  executed after {function.__name__} function.")

    return wrapper   # Return FUNCTION itself  &  NOT function execution that is wrapper() WRONG HAI


# EXAMPLE 1 :
def say_hello():
    print("Hello!! How are you ?")


# =======================
# DECORATING THE FUNCTION
# =======================
# Passing function into decorator
new_func1 = decorators(say_hello)

# Calling wrapper function
new_func1()



print('\n')


# EXAMPLE 2 :
def animal():
    print(f"The name of animal is Lion.")

# =======================
# DECORATING THE FUNCTION
# =======================
# Passing function into decorator
new_func = decorators(animal)

# Calling wrapper function
new_func()

print("\n")

# Therefore we can say decorators is a function that takes a predefined(not necessary) function as parameter ----> creates a new function(wrapper) containing the parameter function inside it's body. Then returns that new function(wrapper).


# =========================================================
# DECORATOR SHORTCUT SYNTAX
# =========================================================

@decorators
def hello():
    print("Hello from shortcut decorator!")

hello()



