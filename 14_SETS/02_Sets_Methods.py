# SET METHODS

# Creating a set (unique + unordered collection)
my_set = {12, 22, 33, 45, 56, 78}

print(f"The elements inside set are: {my_set}")


# 1. ADD
# Adds a single element to the set
my_set.add(88)
print("After add:", my_set)


# 2. REMOVE : Removes the element
# Throws KeyError if element not found
my_set.remove(56)
print("After remove:", my_set)


# 3. DISCARD : Removes element if present
# Does NOT throw error if element is missing
my_set.discard(1)                            # no error even if 1 not present
print("After discard:", my_set)


# 4. POP : Removes and returns an arbitrary element (not fixed)
removed_item = my_set.pop()
print("Removed element:", removed_item)
print("After pop:", my_set)


# 5. LENGTH
print("Size of set:", len(my_set))

# 6. CLEAR : Removes all elements
my_set.clear()
print(my_set)

