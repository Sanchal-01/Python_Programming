# break is a loop control statement.
# The Break statement is used to exit a loop prematurely.

for i in range (1, 10):
    if i == 7:
        break   # when i == 7 STOP the execution of the loop completely and exit the loop. Do not execute anything below break inside the loop. 
    print(i)
print("\n")   



for l in range (15, 25):
    if (l < 19):            # When l == 19, "if"  condition becomes false and else condition executes. "Note" : Else koi loop nahi hai wo bas if ka alternative hai.
        print(l)            
    else:                   # Where there's a break statement which forces to get out of the loop completely and do not check for next conditions anymore. like when l=20/21/22 
        break


# Practice Question 1 : Determine O/P
for i in range(1, 6):
    if i == 3:
        break
    print(i)


# Practice Question 2 : Determine O/P
for i in range(1, 6):
    print(i)
    if i == 3:
        break
    print("Hello")

# Practice Question 3 : Determine O/P
for i in range(1, 6):
    if i == 2:
        continue
    if i == 4:
        break
    print(i)

#  Practice Question 4 : Determine O/P
for i in range(0,3):
    for j in range(0,3):
        if j == 1:
            break
        print(i, j)

# --------------------------------------------------------------------------------------------------------------------------------------#
# LEVEL 1 BASIC

# Important Question 1 :
# Write a program which loop 1 to 50, if number divisible by 3 -->skip,if number divisible by 7--> STOP. Print rest of the numbers.

for i in range (1,51):
    if (i% 3== 0):
        continue
    if (i% 7 ==0):
        break
    print(i)



# Important Question 2:  Write a program which Loop from 1 to 20:
# - If the number is even → print "Even",
# - If the number is odd → print the number itself,
# - If the number is 13 → stop the loop completely

for m in range (1, 21):
    if (m % 2 == 0):
        print(f"{m}: Even number")
    else:
        print(f"{m}: Odd number.")  

    if m== 10:
        break
print("\nLoop execution successful.....")
  

# Important Question 3:  Write a program which
# Take numbers from the user continuously.
# If the user enters 0, stop taking input.

value = True
while (value):
    num = int(input("Enter the number: "))
    if num == 0:
        print("Warning, do not enter 0.")
        num = int(input("Enter the number: "))
        if num == 0:
            print("\nThanks but no thanks...P")
            break


# Important Question 3:  Write a program which
# Print numbers from 1 to 100.Stop as soon as you find the first number divisible by 17.

for i in range (1,101):    
    if i % 17 == 0:
        print(f"{i} is divisible by 17, we are stopping.\n")
        break
    print(i)



# Important Question 4:  Write a program which
# Print every character of "Programming". Stop when the character 'g' appears for the first time.

char = "Programming"

for char in char:
    if char == "g":
        print("This is the first g so we are stopping.")
        break
    print(f"{char}")

# --------------------------------------------------------------------------------------------------------------------------------------#
# LEVEL 2 : ADVANCED

# Important Question 1. Search for a number in a list.
# numbers = [15, 22, 9, 45, 31, 18]. If 45 is found, print Found! and immediately stop searching.

numbers = [15, 22, 9, 45, 31, 18]

for numbers in numbers:
    if numbers == 45:
        print("45 found !! Stopping loop execution")
        break

    print(numbers)


# # Important Question 2.
# # Take password input repeatedly.
# Correct password:python123. Keep asking until the correct password is entered.

value = True
while (value):
    password = input("Enter the correct password: ")

    if not password == "python123":
        print("Please, enter the correct password")
        
    if password == "python123":
        print("Access granted.")
        break
    



# Ultimate Challenge

# Without using exit() or quit().
# Create a guessing game.Secret number = 27
# User keeps guessing.
# If guess is correct,Congratulations! and terminate the loop using only break.

value = True
while (value):

    secret_number = 27
    guess = int(input("Enter the number you want to guess: ")) 

    match guess:
        case 10:
            print("Better luck next time")
        
        case 27:
            print("Kya baat hai !! Bilkul sahi jawab.")
            break

        case _:
            print("Bad guess")