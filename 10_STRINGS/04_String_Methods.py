# Note: Strings are immutable (once a string object is created in memory, its content cannot be changed).
# Note: Every function in Python is followed by parentheses (), i.e., function_name().

name = "Sanchal"
print(name[0])

name[0] = "T"
# NO!! I cannot do this (this is a runtime error).
# Strings are immutable; we cannot replace a character in a string directly.
# We can use the existing string to create a new string, but we cannot modify the original string in memory.

n = len(name)   # len() is a function that returns the length of the string.
print(n)

# STRING METHODS

w = "hello world"

# CHANGING CASES 
print(w, w.upper(), sep=" --> ")       # Converts all characters of the string to UPPER_CASE.
print(w, w.lower(), sep=" --> ")       # Converts all characters of the string to lower_case.
print(w, w.capitalize(), sep=" --> ")  # Converts the first character of the string to Upper_case.
print(w, w.title(), sep=" --> ")       # Converts the first character of each word to Upper_Case.


# REMOVING WHITESPACE
naam = " Hellow World "
print(naam.strip())  # O/P: "Hellow World"  # Removes whitespaces(both left and right)
print(naam.lstrip()) # O/P: "Hellow World " # Removes only white space along the left side of text.   
print(naam.rstrip()) # O/P: " Hellow World" # Removes only white space along the right side of text.

# Note: Strip function kabhi bhi print statement mein nahi lagta, hamesha string pe lagta hai.

# FIND and REPLACE
text = "Python is fun and fun & fun"
print(text.find("is"))   # Output: 7   # Finds and returns the position of the first occurence('i' of is) which we are trying to find. 
print(text.replace("fun", "awesome"))  # Output: "Python is awesome"


# SPLITTING and JOINING
text = "apple,banana,orange"
fruits = text.split(",")
print(fruits)

new_text = " / ".join(fruits)
print(new_text) 


# CHECKING STRING PROPERTIES
text = "Python123"
print(text.isalpha())  # Output: False
print(text.isdigit())  # Output: False
print(text.isalnum())  # Output: True
print(text.isspace())  # Output: False

 