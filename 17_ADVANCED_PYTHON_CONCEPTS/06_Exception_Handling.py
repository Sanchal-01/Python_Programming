# EXCEPTION HANDLING AND CUSTOM ERRORS :

# Exceptions are events that occur during the execution of a program that disrupts the normal flow of instuctions.
# Python provides a robust mechanism for handling exceptions using try-except blocks.
# This allows our program to gracefully recover from errors or unexpected situatons, preventing crashes and providing informative messages with the help of except Exception as e:




# Classic example of Infinite Loop:
while True:
    a = int(input("Enter the 1st number of your choise : "))
    b = int(input("Enter the 2nd number of your choise : "))

    print(f"The sum of numbers is : {a+b} ")
    


# Here we know we can receive only integer as our input to perform sum operation.
# If suppose someone enters a string and press enter -----> the entire program would crash at that stage.
# To deal with such situation we will use exception handling ....try and except 

# while True:
    try:
        c = int(input("Enter the 1st number : "))
        d = int(input("Enter the 2nd number : "))

        print(f"The difference  of numbers is : {c-d} ")

    except Exception as e:    # Here e caries the description( more information ) of error.
        print("Something wrong has happened !!", e)

    except:
        print("Something wrong has happened !!")
        


    
# We have now successfully handeled the error. In case we get any error in our try block then code under except block will be executed.
# NOTE: In case of error in try block except block can handle it without crashing the code for other iterations/ Users.


# while True:
    try:
        a = int(input("Enter the 1st number of your choise : "))
        b = int(input("Enter the 2nd number of your choise : "))
        print(f"The division of these numbers : {a/b} ")

    except ValueError as v:
        print("Please do not perform bad typecasting : ",v)

    except ZeroDivisionError as z:
        print("Division by Zero not allowed :", z)

    except Exception as e:                     # For other type of errors
        print("Some error occured", e)

    # Alternative way using tuple of Errors together:
    except (ZeroDivisionError, ValueError) as l:
        print(f"An error occurred: {l}")
    break
# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


# RAISING AN ERROR :

# Whenever we write some custom codes and we want our code to throw certain errors with personalized messages then we can definitely use #RAISE keyword to throw an error.
# This can be done before actual code execution and saves time. 

a = int(input("Enter the 1st number of your choise : "))
b = int(input("Enter the 2nd number of your choise : "))

if b==0:
    raise ValueError("Please do not divide by zero")

print(f"The division of these numbers : {a/b} ")

