# List comprehension = ek line me list create karna using loop + optional condition
# List comprehension = shortcut for loop + append in one line

numbers = [1, 2, 3, 4, 5]

# Traditional way: Preferred when it's required to incease the line on code inside for loop.
squares = []
for i in range(1,6):
    squares.append(i*i)

print(squares)

# List Comprehension way :SQUARING NUMBERS
squares = [i*i for i in range(1,6)]
print(squares)


# Structural Syntax 

# variable = [expression for item in iterable]

# expression -> what operation to perform (i*i)
# item       -> loop variable (i)
# iterable   -> list / range / any iterable object


# For printing even numbers: CONDITION equally important
even_numbers = [i for i in range(10) if i % 2 == 0]
print(even_numbers)


# 1. UPPERCASE COVERSION:  Convert each name to uppercase
names = ["sanchal", "rahul", "amit"]
upper = [name.upper() for name in names]
print(upper)


# 2. FILTER WORDS: Keep only words whose length is greater than 3
words = ["apple", "bat", "cat", "elephant"]
long_words = [w for w in words if len(w) > 3]   
print(long_words)


# 3.Create list quickly: Create list from 1 to 10
numbers = [i*1 for i in range(1,11)]
print(numbers)

