# Args IN PYTHON :
# *args allows a function to accept VARIABLE NUMBER of POSITIONAL ARGUMENTS.
# The name args is just a convention, we can use any valid variable name preceded by a single asterix(e.g. 8values, *numbers). Single asterisk (*) is what matters.

# Positional arguments means: arguments passed according to position.

# Example: 
# func_name(1,2,3)

# Here:
# 1 -> first position
# 2 -> second position
# etc.



# Conceptual Example :

def sum(a,b):
    return (a+b)

print(sum(2,3))
# print(sum(2,3,5,7,8)) 
# But if i want to increase the number of values I want to pass as argument to perform the sum then we can get some error like 
# sum() takes 2 positional arguments but 5 were given. So to rescue from the above situation we usse this thing called *args.


def my_function(*args):
    print(type(args))  # <class 'tuple'>
    for arguments in args:
        print(arguments)

my_function(1, 2, 3, "hello")  # Output: 1 2 3 hello
my_function()  # No output (empty tuple)
my_function("a", "b")  # Output: a b

# In this example, args collect all the positional arguments passed to my_function into the args tuple.
print("\n")




# Example Using *args:
def sum(*args):
    total = 0
    for item in args:    # NOTE  do not put asterix here with args  ----> Do NOT use * while iterating:
        total += item
    return total

print(sum(5,5,6,4),"\n")  # Function can now accept variable number of positional arguments then also our function won't break.




# MIXING NORMAL PARAMETERS + *ARGS:

def student(name,*marks):

    print("Student:",name)
    print("Marks:",marks)

student("Sanchal",80, 90, 95, 100)

