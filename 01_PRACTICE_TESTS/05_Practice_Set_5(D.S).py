# Python Collections – Practice Set
# This set is based on the topics we’ve covered so far:

# - Introduction to Lists
# - List Methods
# - Tuples and Operations on Tuples
# - Sets and Set Methods
# - Dictionaries and Dictionary Methods



# Topic 1:

# 1. Create a list fruits = ["apple", "banana", "cherry"]
# - Print the first fruit.
# - Replace "banana" with "orange"
# - Print length of the list

fruits = ["apple", "banana", "cherry"]
print(f"The list of fruits is: {fruits}")
print(f"The first fruit is : {fruits[0]}")

# fruits["banana"] = "orange"   # NOTE: Wrong Lists indices cannot be string.
fruits[1] = "orange"  
print(f"Updated list : {fruits}") 

print(len(fruits))

print("\n")


# 2. Create a list of numbers from 1 to 10 .
# - Print the first three numbers using slicing.
# - Print the last three numbers using slicing. 

# TRADITIONAL METHOD:
numbers = []
for i in range(1,11):
    numbers.append(i)
print(numbers) 

# USING LIST COMPREHENSION:
numbers = [i*1 for i in range (1,11)]
print(numbers)
print(numbers[0:4])
print(numbers[-5:-1])

#-----------------------#----------------------#------------------#------------------#--------------------#------------------#---------------------#----------------#----------------#

# TOPIC 2. LIST METHODS

# Q1. Start with numbers = [5, 2, 9, 1, 7] and do the following:
#  - Sort the list in ascending order.
#  - Append the number 10 to the list.
#  - Remove the number 2 from the list.
 
list_1 = [5, 2, 9, 1, 7]

list_1.sort()
print(f"The sorted list is : {list_1}")

list_1.append(10)
print(list_1)

list_1.remove(10)
print(list_1)



# Q2. Create a list, names = ["Alice", "Bob", "Charlie"] and use the insert() method to add "David" at index 1.

names = ["Alice", "Bob", "Charlie"]
names.insert(1, "David")

print(f"The updated list of names is {names}")


# insert() is a method that modifies in-place and returns "None" unlike pop() that returns a value which we can store inside a variable.
inserted_item = names.insert(1, "David") 
print("Inserted Item :", inserted_item)
print(names)

#-----------------------#----------------------#------------------#------------------#--------------------#------------------#---------------------#----------------#----------------#

# TOPIC 3. TUPLES and Operations on TUPLES


# Q1. Create a tuple coordinates = (10, 20) and print both elements.
coordinates = (10, 20)
print(coordinates)
print(type(coordinates))


# Q2. Try to modify tuple by setting coordinates[0] = 50. Note what happens.

# coordinates[1] = 25   # Tuple object does not support item assignment.
# print(coordinates)  


# Convert the tuple to a list, change it's firt=st element to 50, and convert it back to a tuple.

sanchal_tuple=(10,35)
print(f"The original tuple is {sanchal_tuple}.")

sanchal_list = list(sanchal_tuple)
sanchal_list[0] = 50
print (f"The transformed list is {sanchal_list}")

sanchal_list = tuple(sanchal_list)
print(f"The transformed list into tuple is {sanchal_list}.")


# #-----------------------#----------------------#------------------#------------------#--------------------#------------------#---------------------#----------------#----------------#

# # TOPIC 4 : SETS & SETS METHODS

# # Q1. Create a set my_set = {1, 2, 3, 4, 3, 5,7 , 7, 8} and print it. (What happens to duplicate 3 & 7 ? )

my_set = {1, 2, 3, 4, 3, 7 ,7 , 8}   
print(my_set)    # Set always print duplicate elements one time.

# Q2. Add 5 to the set, remove 2, and check if 4 is in the set?
my_set.add(5)
my_set.pop()
my_set.copy()
print(my_set)

# Yes 4 is in the set but 1 is not and 5 is added in the set.

print("\n")

# Q3. Create 2 sets: Find there Union, Intersection and Difference.

set_1 = {1, 2, 3, 4}
set_2 = {5, 2, 5 ,6, 7}

c = set_1.union(set_2)
print(c)

d = set_1.intersection(set_2)
print(d)

e = set_1.difference(set_2)
print(e)

#-----------------------#----------------------#------------------#------------------#--------------------#------------------#---------------------#----------------#----------------#

# TOPIC 5 : DICTIONARY & DICTIONARY METHODS

# Q1. Create a dictionary student = {"name": "John", "age": 20, "grade": "A"}
# - print the value of "name"
# - Change "grade" to "A+"
# - Add a new key "city" with value "Delhi"

student = {"name": "John", "age": 20, "grade": "A"}
print(student["name"])

student["grade"] = "A+"
print(student["grade"])

student["city"] = "Delhi"
print(student)

print(student.keys())
print(student.values())

print("\n")

# Q2. Create a dictionary of three friends and their phone numbers. Use:
# -keys() to get all names 
# -values() to get all numbers
# -items() to loop over key-value pairs and print them.

friends = {"Sanchal": 128989735, "Shorya": 983653423, "Shreyash": 121237453}
print(friends.keys())
print(friends.values())
print(friends.items())

#-----------------------#----------------------#------------------#------------------#--------------------#------------------#---------------------#----------------#----------------#

# Bonus Questions: 

# Q1: Write a program that takes a list of numbers and remove all duplicates using a set.

# Taking integer input
list_1 = list(map(int, input("Enter numbers separated by space: ").split()))

# Taking string input
list_1 = input("Enter numbers separated by space: ").split()
Without_duplicates = set(list_1) 
sorted_numbers = sorted(Without_duplicates)                 # How can i arrange the set of numbers in ascending order?

print(f"The list of numbers without duplicate is{sorted_numbers}.")


print("\n")


# Q2. Given a dictionary with products and its prices find the product with highest price.
products = {"AC": 30000, "Air Cooler":10000, "Fan":900, "Refrigerator":55000}

def highest_price_product():
    
    # max() finds the key having highest value
    product = max(products, key = products.get)       # Find the dictionary key whose value is maximum.
    
    return product

print(highest_price_product())

