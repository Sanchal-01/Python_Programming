# REDUCE FUNCTION IN PYTHON
# The reduce () function applies a function of two arguments cumulatively to the items of an iterable, from left to right , so as to reduce the iterable to a single value.
# reduce () is not a built in function ----> it must be imported from the functools module.

# Syntax : reduce(function, iterable[, initializer])
# function : A function that takes two arguments.
# iterable : The iterable to be reduced.
# initializer (optional): If provided, it's placed before the items of the iterable in the calculation and serves as a default when the iterable is empty.


from functools import reduce

num_list = [1, 3, 2, 4, 7, 4, 1, 4]
#          [4, 2, 4, 7, 4, 1, 4]
#          [6, 4, 7, 4, 1, 4]
#          [10, 7, 4, 1, 4]               # This is how reduce function worksin python.
#          [17, 4, 1, 4]
#          [21, 1, 4]
#          [22, 4]
#          [26]


def sum(a, b):
    return a + b

c = reduce(sum, num_list)
print(c)





numbers = [1, 2, 3, 4, 5]

# Calculate the sum of all numbers using reduce
sum_of_numbers = reduce(lambda x, y: x + y, numbers)
print(sum_of_numbers)  # Output: 15


# Equivalent using a loop (for sum):
total = 0
for x in numbers:
    total += x    # Value of x increments one by one from 1-->2-->3-->4-->5
print(total)      # 15


# Calculate the product of all numbers using reduce
product_of_numbers = reduce(lambda x, y: x * y, numbers)
print(product_of_numbers)  # Output: 120



#reduce with initializer
empty_list_sum = reduce(lambda x,y: x+y, [], 0)
print(empty_list_sum) # 0

# Without the initializer:
# empty_list_sum = reduce(lambda x,y: x+y, []) # raises TypeError




