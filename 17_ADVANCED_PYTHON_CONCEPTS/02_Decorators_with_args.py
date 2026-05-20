# =========================================================
# DECORATORS WITH ARGUMENTS
# =========================================================

# If original function takes arguments, wrapper must also take arguments.


def smart_decorator(function):

    def wrapper(name):

        print("Before function")

        function(name)

        print("After function")

    return wrapper


@smart_decorator
def animal(name):
    print(f"The animal name is {name}")

animal("Lion")


#----------------------------------------------------------#----------------------------------------------------------#----------------------------------------------------------#


# EXAMPLE 2:
def repeat(n):
    def decorator(func):
        def wrapper(name):
            for i in range(n):
                func(name)
        return wrapper
    return decorator

@repeat(7)
def say_hello(name):
    print(f"My name is {name}.")

say_hello("Sanchal")


# This boils down to : It replaces the function say_hello with 
'''
def decorator(func):
    def wrapper(name):
        for i in range (n):
            say_hello(name)
        return wrapper
    return decorator
'''