# Tuples are ordered but immutable collections (cannot be changed after creation).
# Creating Tuple:

my_tuple = (10, 20, 30)
print(my_tuple)



# Tuple with one element (comma required)
# (5) → sirf 5  
# (5,) → tuple with one element

n = input("Enter the single tuple of your choise : ")
print(f"You have entered {n}")
single_element = (n,)    
print(f"The single element tuple is {single_element}")



# Accessing Tuple Elements :
# The accessing procedure of an element in a TUPLE is same as it was in the case of LIST

tup =   (12, 2, 34, 56, 5, 4)
#index=  0   1  2   3   4  5  
print(f"The tuple at index {2} is :{tup[2]}")
print(type(tup[2]))



# tup[3] = 33   # TypeError: 'tuple' object does not support item assignment