# SET OPERATIONS

# There are mainly 3 basic operations in sets:
# 1. UNION
# 2. INTERSECTION
# 3. DIFFERENCE

a = {3, 4, 56, 23, 78}
b = {2, 56, 67, 98, 90, 23}


# 1. UNION
# Combines elements from both sets & Removes duplicates automatically
c = a.union(b)
print("Union:", c)


# 2. INTERSECTION
# Returns only common elements present in both sets
d = a.intersection(b)
print("Intersection:", d)


# 3. DIFFERENCE
# Returns elements present in 'a' but NOT in 'b'
e = a.difference(b)
print("Difference (a - b):", e)