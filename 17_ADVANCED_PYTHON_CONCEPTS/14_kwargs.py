# **kwargs (Keyword Arguments)
# **kwargs collects any extra keyword arguments passed to a function into a dictionary.

# Keyword Arguments mean:
# parameter = value
# Example: name="Sanchal"


# Here:
# name → keyword
# Sanchal → value

# IMPORTANT: kwargs is only a convention. These are also valid: **data, **options, **student_info. The DOUBLE ASTERISK (**) is important.
# BASIC EXAMPLE

def marks(**kwargs): # kwargs becomes a dictionary
    print(type(kwargs))

    # Iterating dictionary
    for key, value in kwargs.items():
        print( f"The marks of {key} is {value}")

marks(Shantanu=99, Vikram=57, Sanchal=95)



# WHY we use **kwargs ?

# Without kwargs:
def student(name, marks):
    print(name, marks)

# Works:
student("Sanchal",95)

# But:
# student(
#     name="Sanchal",
#     marks=95,
#     age=20
# )

# ERROR



# Using kwargs:

def student_info(**kwargs):
    for key,value in kwargs.items():
        print(key,":",value)

student_info(name="Sanchal", age=20, city="Bhopal", marks=95)


print("\n")





def marks(**kwargs):
    # kwargs is a dictionary with all the key value pairs which were passed to marks.

    for item in kwargs.keys():
        print(f"The marks of {item} is {kwargs[item]}")

marks(Shantanu= 99, Vikram= 57, Sanchal= 95)




# MIXING NORMAL PARAMETERS + KWARGS

def employee(department, **kwargs):
    print("Department:",department)
    print(kwargs)


employee("IT",name="Alice",salary=50000)



# =====================================================
# IMPORTANT NOTES
# =====================================================

# 1. **kwargs collects EXTRA keyword arguments.
# 2. kwargs becomes a dictionary.
# 3. kwargs is NOT special name.
# 4. ** is special.
# 5. Use .items() when iterating.
# 6. Useful when number of inputs is unknown.


# =====================================================
# FINAL DEFINITION
# =====================================================
# **kwargs allows a function to accept
# variable number of keyword arguments
# by collecting them into a dictionary.