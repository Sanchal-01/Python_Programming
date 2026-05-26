# map is higher order functions in python and many other programming languages that operate on iterables(lists, tuples).
# They provide a concise and functional way to perform common operations on sequences of data without using explicit loops. 


# Map Function:
# The map () function applies a given function to each item of an iterable and returns an iterator that yields the results.

# Syntax: map(function, iterable, ......)

numbers = [1, 22, 3, 4, 7, 9, 10]

def square(x):
    return x * x

new = map(square, numbers)         # By default it creates a map object and stores this value into variable.
 
new = tuple(map(square, numbers))
new = list(map(square, numbers))   # To see the value of map output we have to covert it into list.
print (new)



numbers = [1, 2, 3, 4, 5]


# Square each number using map via Lmbda function :
squared_numbers = map(lambda x: x**2, numbers)
print(list(squared_numbers)) 



# Example with multiple iterables
numbers1 = [1, 2, 3]
numbers2 = [4, 5, 6]
summed = map(lambda x, y: x + y, numbers1, numbers2)
print(list(summed)) 


# Equivalent list comprehension:
squared_numbers_lc = [x**2 for x in numbers]
print(squared_numbers_lc)   # Output: [1, 4, 9, 16, 25]