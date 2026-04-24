
# TUPLE METHODS IN PYTHON

# A tuple is an ordered, immutable collection of elements.
# Immutable means: once created, elements cannot be changed.

# Creating a tuple
First_Tuple = ("Sanchal", 21, 11)
print(First_Tuple)



# count() METHOD
# count(value) → returns how many times a value appears in the tuple

print(f"The number of occurrences of 'Sanchal' is: {First_Tuple.count('Sanchal')}")


# index() METHOD
# index(value) → returns the index (position) of the first occurrence of the value

print(f"The index of 11 is: {First_Tuple.index(11)}")



# SHORT METHOD OF USING TUPLE:

# We can directly create a tuple and apply a method without storing it
# This creates a tuple (1, 2, 2, 3) and counts how many times 2 appears

tuple_count = (1, 2, 2, 3).count(2)

print(tuple_count)



# WHY USE TUPLES?

# 1. Immutable = safer data (cannot be changed accidentally)
# 2. Faster than lists (slightly better performance)
# 3. Used for fixed data (like coordinates, records, etc.)
# 4. Can be used as dictionary keys (lists cannot)