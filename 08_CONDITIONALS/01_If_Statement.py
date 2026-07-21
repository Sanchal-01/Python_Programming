# An "if" statement in Python runs a specific block of code only if a condition is True.

age = 21

if (age> 12):
    print("My name is Sanchal")
    print ("What's your name ??")

print("This is outside if statement and will be printed in any case whether if condition is satisfied or not. ")

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

# 1. The Movie Ticket Scanner
# Task: Ask the user for their age using input(). If they are 18 or older, print "Access Granted. Enjoy the movie!".
# Otherwise, print "Access Denied. You must be 18 or older."


while True:
    age = int(input("Please enter your age:"))

    if age >= 18:
        print("Access Granted. Enjoy the movie!")
        continue
    print("Access Denied. You must be 18 or older.")

# In the above example I have automated the input statement to ask user enter their age user after user using while True.
# Used continue after the if statement to skip that iteration so that the below code is not executed.
# The "Access denied" code is executed only when user enters the age not fulfilled by if statement.