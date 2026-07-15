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



# Just trying something new O_O :
user_input = input("Enter your name : ").lower()
while user_input != "exit":
    print(f"You have a nice name, {user_input}")
    user_input = input("Enter your name : ").lower()  # This stops the infinite loop

print("Thanks for telling your name.")
