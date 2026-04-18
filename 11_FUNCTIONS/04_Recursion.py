# A function calling itself to solve a problem.


'''
FIBONACCI SERIES : 0 1 1 2 3 5 8 13
Fib INDEX:         0 1 2 3 4 5 6 7......

fib(0) = 0
fib(1) = 1
fib(2) = fib(0) + fib(1)
fib(3) = fib(1) + fib(2)
fib(4) = fib(2) + fib(3)

fib(n) = fib(n-2) + fib(n-1)

'''
def fib(n):
    if (n==0 or n==1):  # Base case of recursion
        return (n)
    
    return (fib(n-2) + fib(n-1))

value= fib(6)
print(value)

# Important NOTE:
# Must have a base case to avoid infinite recursion.
# Used in algorithms like Fibonacci, Tree Traversals.

'''
# How fibonacci for fib(6) is calculated

fib(4) + fib(5)
fib(2) + fib(3) + fib(5)
fib(0) + fib(1) + fib(3) + fib(5)
0 + 1 + fib(1) + fib(2) + fib(3) + fib(4)
0 + 1 + 1 + fib(0) + fib(1) + fib(1) + fib(2)+ fib(4)
0 + 1 + 1 + 0 + 1 + 1 + fib(0) + fib(1) + fib(2) + fib(3)
0 + 1 + 1 + 0 + 1 + 1 + 0 + 1 + fib(0) + fib(1) + fib(3)
0 + 1 + 1 + 0 + 1 + 1 + 0 + 1 + 0 + 1 + fib(1) + fib(2)
0 + 1 + 1 + 0 + 1 + 1 + 0 + 1 + 0 + 1 + 1 + fib(0) + fib(1)
0 + 1 + 1 + 0 + 1 + 1 + 0 + 1 + 0 + 1 + 1 + 0 + 1

'''

#-----------------------------------#--------------------------------------------#---------------------------------------#----------------------------#

'''
Factorial Using Recursion:
FACTORIAL : 0 1 2 6 24 120 
INDEX :     0 1 2 3  4  5  .... 

fac(0) = 1
fac(1) = 1
fac(2) = fac(1)*(2)
fac(3) = fac(2)*(3)
fac(4) = fac(3)*(4)

fac(n)= fac(n-1)*(n)

'''
def fac(n):
    if(n==0 or n==1):   # Base case of recursion. Function must have a base case to avoid infinite recursion.
        return 1
    return(fac(n-1)*(n))

ans =fac(4)
print(ans)


# Function must have a base case to avoid infinite recursion.
# If by any chance we forget to mention the base class it would lead to FILLING STACK and MEMORY can cause StackOverflow & other Memory Errors.