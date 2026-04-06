# Indexing is the process of accessing a specific element within an iterable(such as a string, list, or tuple) by referring to its position.
name = "HAPPY"

# name = " H  A  P  P  Y "
# index    0  1  2  3  4     # Note : In programming indexing starts from 0.   # If there are n charaters in the string, value of last index would be (n - 1). Here (n-1)= 4.                         
# index   -5 -4 -3 -2 -1     

print(name[0])
print(name[1])
print(name[2])
print(name[3])
print(name[4])

print(name[-1])  # Whenever -ve index is encountered --> Try converting it to positive index.
print(name[-2])  # E.g. name[-2 + 5] = name[3]. Here '5' is the length of string.
print(name[-3])
print(name[-4])
print(name[-5])
