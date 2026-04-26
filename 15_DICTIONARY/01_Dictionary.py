# DICTIONARY in Python

# Dictionaries store data in key-value pairs.
# - Keys must be unique
# - Values can be duplicate
# - Dictionary is mutable (can be changed)
# - Provides fast lookup using keys

# DICTIONARY CONCEPTS

# While creating a dictionary:
# - Keys must be UNIQUE and HASHABLE (immutable)
# - Values can be of any data type

# Hashable data types: int, float, str, tuple
# Not hashable: list, dict, set

# Creating dictionaries
Age = {"Sanchal": 20, "Harry": 34, "Rama": 25, "Suresh": 34}  # Duplicate VALUES allowed, KEYS must be unique
Marks = {"Sanchal": 97, "Harry": 98, "Rama": 100}

print(Age, type(Age))


# Accessing values using keys
print(Marks["Sanchal"])   # Output: 97

# print(Marks[0])  Not allowed (no indexing in dictionary)


# Modifying values
Marks["Sanchal"] = 99   # Updating existing value
print("Updated Marks:", Marks)


# Adding new key-value pair
Marks["Rohit"] = 85
print("After adding new entry:", Marks)


print("\n")

# IMPORTANT:
# Accessing a non-existing key will give KeyError
# print(Marks["Unknown"]) 

# Getting all keys and values
print(Marks.keys())
print(Marks.values())
print(Marks.items())

print("\n")

# Safe way using get()
print(Marks.get("Unknown"))     # Output: None (no error)
print(Marks.get("Unknown", 0))    # Output: If "Unknown" ----> 0 (no error)