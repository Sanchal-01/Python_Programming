# TYPES OF ARGUMENTS:
#-----------------------#----------------------#------------------#------------------#--------------------#------------------#---------------------#----------------

# 1. POSITIONAL ARGUMENT:

def number(a, b, c):     # Here a, b, c are called PARAMETERS.
    operation = a-b-c
    return operation


z = number(5, 3, 1)    # Here 5, 3, 1 are called POSITIONAL ARGUMENTS beecause these are the real values which are being passed to the parameters of variables of the function.
print(z)


#-----------------------#----------------------#------------------#------------------#--------------------#------------------#---------------------#----------------


# 2. DEFAULT ARGUMENT:

# Example 1:
def greet(name="Guest"):
    return(f"Hello,{name}!!") 

print(greet())            # Here the default argument is executed.
print(greet("Sanchal"))   # Here the default argument is over-written with new ARGUMENT "Sanchal".


# Example 2:
def calc(a, b, plus=2):      # The default argument equals "2" to parameter "plus" has been executed. 
    return (a + b + plus)

print(calc(2, 3))            # NOTE: We haven't passed the value of Para- plus in the function call/ argument assignment.

# NOTE : Default Parameter/argument is always written after - Positional Parameter.

#-----------------------#----------------------#------------------#------------------#--------------------#------------------#---------------------#----------------


# 3. KEYWORD ARGUMENT:

# Example 1:
def sum(a, b, c):
    return(a*b+c)

print(sum(c=10, a=2, b=30)) # Here I have passed the argument in random order because I have assigned proper "Parameter = Argument" FORMAT.
print(sum(2, 30, 10))       # Here I have kept the "Order of Argument" according to the "Order of Parameter" to get correct result.

