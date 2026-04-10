# STRING FORMATTING
# String formatting is a powerful feature in Python allowing us to insert variables and expressions into strings in a structured way.
# Python provides multiple ways to format strings, including the older '.format()' method and the modern 'f-strings'.
 
# METHOD 1:
# Using .format() Method: The .format() method allows inserting values into placeholders {}:

name = "Sanchal"
age= 20
name_2="Ram"
age_2= 21
print("My name is {} and I am {} years old.". format(name,age))
print("My name is {} and I am {} years old.". format(name_2,age_2))

# EXAMPLE 2 :
a= "Ramu"
a1= 20000
b ="Harish"
b1 = 2400
c="Triggerred"
c1= 120000
print("{} you are a good person, I am giving ${} bag to you.".format(a,a1))
print(f"{b} you are a good person, I am giving ${b1} bag to you.")

# We can also specify positional and keyword arguments:
print("{1} is learning {0}".format("Python", "Alice"))  # Output: Alice is learning Python
print("{name} is {age} years old".format(name="Bob", age=25))


# METHOD 2:

# Using 'f-Strings' (Formatted String Literals): Introduced in Python 3.6, f-strings are the most concise and readable way to format strings:
name ="KUMAR"
age = 23
print(f"My name is {name} and I am {age} years old.")


# CHARACTER ENCODING
print(ord('A'))  # Output: 65 ASCII value of Uppercase 'A': 65 / Lowercase 'a': 97
print(chr(65))   # Output: 'A'