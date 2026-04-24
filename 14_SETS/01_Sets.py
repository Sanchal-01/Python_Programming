# SET in Python

# When we store elements inside {}, Python creates a set.
# A set is an unordered collection of unique elements.

# NOTE:
# - Sets do NOT maintain any fixed order (unordered).
# - Elements are NOT accessed using index (unindexed).
# - Duplicate values are automatically removed.

S = {12, 33, 4, 5, 5, 5, 66}    

print(S, type(S))         # O/P : {33, 66, 4, 5, 12} <class 'set'>

# NOTE:
# We cannot access elements using indexing like list/tuple
print(S[0])  # TypeError: 'set' object is not subscriptable

# IMPORTANT:
# Sets may appear in a certain order while printing,
# but that order is NOT guaranteed and can change.