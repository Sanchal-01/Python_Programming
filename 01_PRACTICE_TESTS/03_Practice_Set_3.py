# CONCEPT 1: Basic String Operations

# Task 1 : Create a string variable "name" with your full name. Print:
# The first character,
# The last character and 
# The length of the string

name = 'Sanchal Kumar'
print(name[0],name[12])
print("Lenght of name is :",len(name))


# Task 2: Concatenate two strings: "Hello" and "World" with a space in between.
str1= "Hello"
str2= "World"
Final_String= str1 + " " + str2
print(Final_String) 

#-----------------------#----------------------#------------------#------------------#--------------------#------------------#---------------------#----------------------#-------------------#----------------------#


# CONCEPT 2 : String Slicing and Indexing

# TASK 1 : Given text = "Python Programming", do the following:
# Print the first 6 characters
# Print the last 6 characters
# Print every second character from the string

text= "Python Programming"
print(len(text))                        # First find the lenght of string. Not specifically needed here.
print(text[:7],text[-6:])               # text[0:7]---> First 6 characters, text[-6,last character]----> Last 6 characters

# TASK 2: Reverse the string text using slicing.
print(text[18::-1])                     # Remember to write the no. of characters of strings to reverse and use "Double colons" '::' in between. 


#-----------------------#----------------------#------------------#------------------#--------------------#------------------#---------------------#----------------------#-------------------#----------------------#

# CONCEPT 3: String Methods and Functions

# TASK 1: Take the string "  i love python programming  " and:
# Remove extra spaces from both ends
# Convert it to title case
# Count how many times "o" appears

Open_to_All="  I love python programming  "
print(Open_to_All,Open_to_All.strip(),sep="---> ")             # Remember in other tools we use TRIM to remove spaces but here we use "variable_name.STRIP()"
print(Open_to_All,Open_to_All.title(),sep="---> ")
print(Open_to_All.count("o"))



# TASK 2: Check if the string "123abc" is alphanumeric.
print(Open_to_All.isalpha())         # Would return true only if the string has only alphabets i.e. no spaces and no numbers.

#-----------------------#----------------------#------------------#------------------#--------------------#------------------#---------------------#----------------------#-------------------#----------------------#


# CONCEPT 4 : String Formatting and f-Strings

# TASK 1: Using format() & f"string", create a sentence:"My name is John and I am 25 years old."by passing "John" and 25 as variables.
name = "Sanchal"
age = 21
print("My name is {} and I am {} years old".format(name,age))   # Function ko call karte samay comma nahi use karna hai  .  use karna hai

print(f"My name is {'Sanchal'} and I am {21} years old.")

#-----------------------#----------------------#------------------#------------------#--------------------#------------------#---------------------#----------------------#-------------------#----------------------#

