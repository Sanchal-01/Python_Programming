# Lists are ordered, mutable (changeable) collections of items.
# Items can be of any data type (int, float, bool, string, etc.)

# MUTABLE - We can add, remove, or modify elements in a list.

List_1 = [1, 2, 34, 55, 123, 128, 45]
# index =   0  1   2   3   4    5    6

# NOTE: Lists can store multiple data types or multiple values of the same data type.

Mixed_List = [21, "Sanchal", 7.0, True]

print(Mixed_List)

# Accessing elements using index (index starts from 0)
print(Mixed_List[1])   # Output: "Sanchal"

print("\n")



# SLICING

# Slicing a list:
# It is used to extract a portion (sublist) from a list without modifying the original list.

# Syntax:
# list[start : end : step]

Mixed_List = [21, "Sanchal", 6.9, False]

# From index 1 to 4 (excluding 5)
print(Mixed_List[1:5])

# From index 0 to 4 with step = 1 (no skipping)
print(Mixed_List[0:5:1])

# From index 0 to 4 with step = 3 (skip 2 elements each time)
print(Mixed_List[0:5:3])
