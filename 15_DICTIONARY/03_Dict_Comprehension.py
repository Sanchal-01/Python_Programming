# DICTIONARY COMPREHENSION

# Dictionary comprehension is a concise (short) way to create dictionaries
# using a single line of code instead of traditional loops.

# It works similar to list comprehension but creates key-value pairs.

# SYNTAX:
# {key_expression : value_expression for item in iterable (optional condition)}

# Example:
# {x: x**2 for x in range(5)}
# Here:
# - x → key
# - x**2 → value
# - range(5) → iterable



# 1. BASIC EXAMPLE - SQUARES

squares = {x: x**2 for x in range(5)}
print("Squares:", squares)
# Output: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
 

# 2. MULTIPLICATION TABLE (TABLE OF 5)

table_of_5 = {x: 5*x for x in range(5)}
print("Table of 5:", table_of_5)
# Output: {0: 0, 1: 5, 2: 10, 3: 15, 4: 20}



# 3. USING CONDITION (FILTERING)

# Only even numbers
even_squares = {x: x**2 for x in range(10) if x % 2 == 0}
print("Even Squares:", even_squares)
# Output: {0: 0, 2: 4, 4: 16, 6: 36, 8: 64}



# 4. VALUE TRANSFORMATION (REAL USE CASE)

names = ["sanchal", "rahul", "amit"]

# Convert values to uppercase
upper_dict = {name: name.upper() for name in names}
print("Uppercase Names:", upper_dict)
# Output: {'sanchal': 'SANCHAL', 'rahul': 'RAHUL', 'amit': 'AMIT'}


# ----------------------------------------
# 5. ANOTHER USE CASE - LENGTH OF WORDS
# ----------------------------------------

words = ["apple", "bat", "cat", "elephant"]

word_length = {word: len(word) for word in words}
print("Word Lengths:", word_length)
# Output: {'apple': 5, 'bat': 3, 'cat': 3, 'elephant': 8}


# ----------------------------------------
# IMPORTANT NOTES
# ----------------------------------------
# 1. Keys must be UNIQUE (duplicate keys will overwrite previous values)
# 2. Values can be anything (int, string, list, etc.)
# 3. Improves code readability and reduces lines of code
# 4. Widely used in data processing (important for Data Analyst role)



# COMPARISON (LOOP vs COMPREHENSION)

# Normal way:
square_dict = {}
for x in range(5):
    square_dict[x] = x**2

print("Using loop:", square_dict)

# Comprehension way (short + clean):
square_dict2 = {x: x**2 for x in range(5)}
print("Using comprehension:", square_dict2)