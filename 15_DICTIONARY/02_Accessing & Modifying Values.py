# DICTIONARY - Accessing & Modifying Values

# Creating a dictionary
student = {
    "name": "Alice",
    "age": 21,
    "grade": "A",
    "city": ("Los Angeles")
}

# # Accessing value using key
# print(student["name"])          # Output: Alice


# # Updating existing values
# student["age"] = 22                  # Update age
# student["city"] = "New York"         # Update city


# # NOTE:
# # If key already exists → value is UPDATED
# # If key does not exist → new key-value pair is ADDED

# # Example of adding new key
# student["country"] = "USA"


# # Final dictionary
# print("Updated student data:", student)


# Safe access using get()
print(student.get("grade"))       # A
print(student.get("city", 0))    # None (no error)| Since "Salary" KEY does not exists------> 0 