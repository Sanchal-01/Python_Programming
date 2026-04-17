# Lambda functions are anonymous, inline functions. 
# So whenever we want to define a function in a line we use LAMBDA function.

square = lambda x: x*x

'''
As good as writing:
def square(x):
    return(x*x)
'''
print(square(3))


sum = lambda x,y: x+y
'''
As good as writing:
def sum(x, y):
    return(x + y)
'''
print(sum(3,11))


# So overall LAMBDA fumction help us to write multiple lines of code of function in one line only.