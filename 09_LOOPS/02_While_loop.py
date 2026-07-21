# WHile loops execute a block of code as long as condition inside the loop is True.
# This loop is useful when number of iterations are not known in advance Unlike "for" loop where the number of iterations are known as range.

# Example : Print number from 1 to 5 

m = 1         
while(m < 5):  
    print(m)  
    m = (m + 1)  
               
# DRY RUN EXPLANATION

# Took value of m = 1
# Loop starts: Condition (m<5) At start m=1 -> print(1) -> now increment value of m +1. Now go back at the start of the loop.
# Now m = 2 -->Check condition (m<5) true, since(2<5) --> print (2)   --> now increment value of m, +1. Now go back at the start of the loop.
# Now m = 3 -->Check condition (m<5) true, since(3<5) --> print (3)   --> now increment value of m, +1. Now go back at the start of the loop.
# Now m = 4 -->Check condition (m<5) true, since(4<5) --> print (4)   --> now increment value of m, +1. Now go back at the start of the loop.

# Now m = 5 -->Check condition (m<5), since(5<5) FALSE  --> Therefore as soon as condition becomes false the command inside loop is not executed and loop exits.


# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

g = 10

while (g > 5):
    print(f"Okay..{g}")

    g = g - 1

    if g == 6:
        break
print("Loop Terminated Successfully....")

# In this example we have used three concepts, C1 : Initialized loop with a condition (g > 5)
#                                              C2 : Increment/ decrement the value of g (g -= 1)
#                                              C3 : For peaceful loop termination we have set decided to break the loop at a paticular value using if control statement. 

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

# Just trying something new O_O :
user_input = input("Enter your name : ").lower()
while user_input != "exit":
    print(f"You have a nice name, {user_input}")
    user_input = input("Enter your name : ").lower()  # This stops the infinite loop

print("Thanks for telling your name.")




# Just trying to include multiple loop concept into one example:

try: 
    user_input = input("Enter your correct age: ").lower()
 
    while user_input != "exit":
        
        user_age = int(user_input) 
        print(f"Your age is, {user_age} \n")

        if user_age <= 18:
            print("You are a child, prohibited vehicle allowance")

        else:
            print("You are an adult, allowed to drive a vehicle.")

        user_input = input("Enter your correct age: ").lower()  # This stops the infinite loop

    print("Thanks for telling your age")

except Exception as Reason:
    print("There's an Error:- ", Reason)