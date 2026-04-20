# Python Function and Modules - Practice Set
# This set is based onthe topics we've covered so far:
# - Defining Functions in Python
# - Function Arguments & Return Values
# - Lambda Functions in Python
# - Recursion in Python
# - Modules and Pip – Using External Libraries
# - Variable Scope and Docstrings



# 01 - Defining Functions

# Q1. Write a function 'greet()' that prints "Hello, Python Learner!" when called.
def greet():
    print("Hello, Python Learner!")        # Simply implemented what was asked in the question.
greet()

def greet(name):
    return(f"How are you {name} ?")        # Tried to make solution bit more creative by passing a parameter to the greet function.

print(greet("Sanchal")) 


# Q2. Write a function square(num) that returns the square of a given number.Test it with different numbers.

def square(num):
    return(f"The square of {num} is {num*num}")   # Most optimized way with correct formatting
    return(f"The square of {num} is",num*num)     # Not a good format because - (value1, value2) ---> Brackets + comma → tuple --> O/P = ('The square of 4 is', 16)

    print("The square of", num, "is", num*num)    # Also a good way but do not provide a return value for assigning it to a new variable.

print(square(4))

#-----------------------#----------------------#------------------#------------------#--------------------#------------------#---------------------#----------------#----------------#


# 02 Function Arguments & Return Values

# Q1. Write a function full_name(first, last) that takes first name and last name as parameters and returns a single string in the format "First Last".

def full_name(first, last):
    return(first + last)
print(full_name("Sanchal"," Upadhyay"))

def full_name(first, last):
    return(f"My full_name is {first + last}")              # Bit curious BTW :)
print(full_name("Sanchal"," Upadhyay"))


# Q2. Write a function calculate_area(length, width) that returns the area of a rectangle. Test it by calling the function with:
# - Both length and width
# - Only length (use default width)

def calculate_area(length, breadth=20):
    return (f"The area of rectangle is {length*breadth}.")
print(calculate_area(10, 10))    
print(calculate_area(10))


#-----------------------#----------------------#------------------#------------------#--------------------#------------------#---------------------#----------------#----------------#

# 03 Lambda Functions

# Q1 Write a lambda function that adds two numbers and test it.
sum = lambda x,y : (f"The sum of {x} and {y} is: {x+y}")
print(sum(2,5)) 

# Q2. Create a list [1, 2, 3, 4, 5] and use map() with a lambda function to get their squares.

square = lambda x: x*x
my_list= [1,2,3,4,5,6,7,8]
print(map(square, my_list))
print(list(map(square, my_list)))         # Here we typecasted the map into LIST

print("\n")

#-----------------------#----------------------#------------------#------------------#--------------------#------------------#---------------------#----------------#----------------#

# 04 Recursion in Python

# Q1. Write a recursive function factorial(n) that returns the factorial of a number.

# factorial(0) = 1
# factorial(1) = 1
# factorial(2) = factorial(1) * 2
# factorial(3) = factorial(2) * 3
# factorial(4) = factorial(3) * 4
# factorial(n) = factorial(n-1) * n

def factorial(n):
    if(n==0 or n==1):
        return(1)

    return(factorial(n-1) * n)
print(factorial(5))



# Q2. Write a recursive function sum_of_digits(n) that returns the sum of all digits of a given number.


def sum_of_digits(n):
    if n < 10:            # base case
        return n
    return (n % 10) + sum_of_digits(n // 10)

print(sum_of_digits(122))


print("\n")
#-----------------------#----------------------#------------------#------------------#--------------------#------------------#---------------------#----------------#----------------#

# 05. Modules and Pip – Using External Libraries

# Q1.Import the math module and use it to:
# -Find the square root of 144
# -Calculate sin(90°) (hint: use math.radians())
# -Find the square of 5.

import math
def squareroot(num,num2):
    return(math.sqrt(num),math.radians(num2))
print(squareroot(144,90))

# NOTE:f-string Syntax: Inside our f-string, if we have a comma and math.pow outside of the curly braces it would become tuple.
# Everything we want to calculate inside an f-string needs to be within {}.


import math
def squareroot(num,num2):
    return(f"The square root of {num} is---> { math.sqrt(num)} and sin({num2}) is---> {math.radians(num2)}")
print(squareroot(144,90))


import math
def power(x,y):
    return (f"The square of {x} is: {math.pow(x,y)}")       # Meaning x is raised to the power of y.
print(power(5,2))


# Tuple vs String: If we try to use sep=" " inside a return statement. 
# NOTE: In Python, sep is an argument for the print() function, not for strings or tuples.
# By using commas, we're actually returning a tuple containing three separate items.



# Q2. Install and import the requests module (if available) and use it to fetch data from "https://api.github.com".

import requests
import requests

# The URL you want to fetch data from
url = "https://github.com"

try:
    # Send a GET request to the URL
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        data = response.json()  # Parse the response as JSON
        print("Data fetched successfully!")
        print(data)
    else:
        print(f"Failed to fetch data. Status code: {response.status_code}")

except requests.exceptions.RequestException as e:
    # Handle any connection errors
    print(f"An error occurred: {e}")

#-----------------------#----------------------#------------------#------------------#--------------------#------------------#---------------------#----------------#----------------#

# 06. Variable Scope and Docstrings

# Q1. Write a function increment() that has a local variable counter intialized to 0 and increment it by 1 each time it's called.
# Observe whether the value persists across function calls.

def increment(n):
    while(n < n+1):
        print(f"{n} is the number to increment.")
        n = n+1
        break
    return(n)
print(increment(2))

print("\n")

def increment():
    n = 0
    while(n < n+1):
        print(f"{n} is the number to increment.")
        n = n+1
        break
    return(n)
print(increment())
print(increment())  # No the value does not persists across function calls.



# Q2. write a function multiply(a,b) that has a proper docstring explaining what it does.
# Then use help.(multiply) to display the docstring.

def multiply(a, b):
    """
    Multiplies two numbers and returns the result.
    Args: 
        a = First number
        b = Second number 
    Returns:
        Multiplication of first and second number 
    """
    return(a*b)

help(multiply)            # Correct Call: help(multiply) (no quotes, no extra dots) is the standard way to view documentation in the console.
print(multiply(2,3))

print("\n")


#-----------------------#----------------------#------------------#------------------#--------------------#------------------#---------------------#----------------#----------------#


# 07 BONUS CHALLENGE QUESTIONS

# # Q1 Write a rucursive function fibonacci (n) that prints the first n fibonacci numbers.

# # fib(0) = 0
# # fib(1) = 1
# # fib(2) = fib(0) + fib(1)
# # fib(3) = fib(1) + fib(2)
# # fib(4) = fib(2) + fib(3)

# # fib(n) = fib(n-2) + fib(n-1)

def fib(n):
    if(n==0 or n==1):
        return(n)
    return(fib(n-2)+fib(n-1))

# for n in range (0,100):       # 1st Mistake  
#     print(fib(n))
    
num = int(input("Enter number of terms: "))

for n in range(0,num):      # "loop ko num baar chalao aur n &  ko 0 se num-1 tak update karo" ====> when n=0_print fib(0) ; when n=1_print fib(1); when n=2_print fib(2); when n=3_print fib(3)
    print(fib(n))



# Q2. Write a function safe_divide(a, b) that returns the result of a / b, but returns "Cannot divide by zero" if b is 0.

def safe_divide(a, b):
    if (b == 0):
        print("Division by zero !!!! not permitted")
    return(f"The division of {a}/{b} is {a/b}")
print(safe_divide(8,4))


# Q3. Create a function is_even(n) that returns True if n is even else prints n is odd.

def is_even(n):
    if(n % 2 == 0):
        print(f"The number {n} is even.")
    else:
        print(f"The number {n} is Odd.")
    return(n)
is_even(5)


#-----------------------#----------------------#------------------#------------------#--------------------#------------------#---------------------#----------------#----------------#