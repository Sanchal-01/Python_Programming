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

