# TUPLE UNPACKING IN PYTHON

# Tuple unpacking means assigning tuple elements to multiple variables

# Creating a tuple
my_tuple = (12, 34, 56)

# Unpacking tuple into variables:
a, b, c = my_tuple

# Each variable gets corresponding value
print(a, b, c)        # Output: 12 34 56


# Example_1. Basic Example
t = (1, 2, 3)
x, y, z = t
print(x, y, z)



# Example_2. Swap Values
a = 10
b = 20

a, b = b, a
print(a, b)    # Output: 20 10



# Example_3. Unpacking with different data types
person = ("Sanchal", 21, "India")

name, age, country = person

print(name)
print(age)
print(country)


#-----------------------#----------------------#------------------#------------------#--------------------#------------------#---------------------#----------------------#-------------------#----------------------#

# ADVANCED EXAMPLES:

# 1. Using * (Star Unpacking)
numbers = (1, 2, 3, 4, 5)

a, *b = numbers

print(a)  # OUTPUT:  1
print(b)  # OUTPUT: [2, 3, 4, 5]


# 2. Middle unpacking
numbers = (1, 2, 3, 4, 5)

a, *b, c = numbers

print(a)  # OUTPUT: 1
print(b)  # OUTPUT: [2, 3, 4]
print(c)  # OUTPUT: 5


# 3. Ignoring values (_ best practice)
t = (10, 20, 30)

a, _, c = t

print(a)  # 10
print(c)  # 30

# 4. Loop + unpacking
pairs = [(1, 2), (3, 4), (5, 6)]

for x, y in pairs:
    print(x, y)

# 5. Function return unpacking
def get_values():
    return (100, 200)

a, b = get_values()

print("a =", a, "b =", b)


# Palindrome Check

user = int(input("Enter the text to check :"))
reverse = user[::-1]
if (user== reverse):
    print("The string is palindrome")
else:
    print("not a palindrome")