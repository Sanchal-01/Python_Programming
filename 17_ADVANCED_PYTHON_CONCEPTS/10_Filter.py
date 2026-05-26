# The filter () function constructs an iterator from elements of an iterable for which a function returns True.
# In other words, it filters the iterable based on a condition.

# Syntax : filter (function, iterable)

# function : A function that returns True or False for each item. If None is passed, it defaults to checking if the elements is True (truthy value).
# iterable : The iterable to be filtered.



def is_number_greater_34(x):
    if (x > 34):
        return True
    else:
        return False 

    
Actual_List = [1, 2, 3, 4, 5, 6, 35, 77 ,89, 63.4, 12, 74, 53, 88, 34]

New_list = (filter(is_number_greater_34, Actual_List))   # <filter object at 0x0000023582BC55A0>
New_list = list(filter(is_number_greater_34, Actual_List))  # This prints O/P = [35, 77, 89, 63.4, 74, 53, 88]
print(New_list, "\n")


# Lambda function is generally used when we talk about map, filter and Reduce beacause they can be fitted in sigle line.
# Use of lambda function should be avoided when our lambda function is not readable and is creating confuusion in code readability and Maintainable by humans.
New_list = list(filter(lambda x: x>34, Actual_List))
print(New_list, "\n")


# Get even nubers using filter 
even_numbers = filter(lambda x: x % 2 == 0, Actual_List)
print(list(even_numbers))

 

# Example with None as function

values = [0, 1, [], "hello", "", None, True, False]

# If none is passed, filter defaults to checking if the elements is True (truthy value).
truthy_values = filter(None, values)

print(list(truthy_values)) # Output: [1, 'hello', True]