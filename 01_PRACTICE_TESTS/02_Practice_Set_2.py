# Topic 1: If_else Conditional Statement

# Question 1:  
# Write a program that asks the user for a number and prints whether it is positive, negative, or zero.

a = int(input("Enter a number = "))
if (a > 0):
    print(a," is a +ve number")
elif(a== 0):
    print("This is a Zero")
else:
    print("This is a -ve number")


# Question 2:
# Create a program that checks if a person is eligible to vote (age >= 18).

a = int(input("Enter your current AGE _"))
if (a>= 18):
    print("Your are eligible to vote")
else:
    print("Not eligible to vote because you are a child. ")


# Question 3:
# Write a program that takes a number from the user and prints "Even" if it is even, otherwise "Odd".

i = int(input("Enter a number - "))
if (i % 2 ==0):
    print ("Number is divisible by 2. It is EVEN")
else:
    print("Number is not divisible by 2. It is ODD")


#-----------------------#----------------------#------------------#------------------#--------------------#------------------#---------------------#----------------------#-------------------#----------------------#


# Topic 2 : MATCH CASE STATEMENTS 


# Question 1 :Ask the user to enter a day number (1–7) and print the corresponding day of the week using match case.

n = int(input("Hey bro, Enter a nuber b/w 1 to 7 : "))
match n:
    case 1:
        print("This is Monday = Workday :( ")
    case 2:
        print ("This is Tuesday, no worries Enjoy!!")
    case 3:
        print("This is Wedneyday, carry on something interesting work.")
    case 4:
        print("This is Thursday, be happy weekend is closer.")
    case 5:
        print("This is Friday, finally last working day of this week :) ")
    case 6:
        print("This is Saturday, Movie time. ")
    case 7:
        print("This is Sunday, Let's have some quality sleep .")

# Question 2 :
#    Write a program using match case that simulates a simple calculator.
#    ----->  Ask the user for two numbers and an operation (+, -, *, /).
#    ----->  Perform the operation using match case.

a = int(input("Enter the first number:"))
b = int(input("Enter the second number:"))
operation = input("Enter the operation:")
c = a+b
d=  a-b
e=  a*b
f=  a/b
match operation:
    case "+":
        print("The sum of two numbers is ",c)
    case "-":
        print("The difference of two numbers is ",d)
    case "*":
        print("The product of two numbers is ",e)
    case "/":
        print("The division of two numbers is ",f)
     
#-----------------------#----------------------#------------------#------------------#--------------------#------------------#---------------------#----------------------#-------------------#----------------------#


# TOPIC 3: For Loops

# Question 1: Print numbers from 1 to 10 using a for loop.

for i in range (1,11):
    print("The  number is",i)


# Question 2: Print the multiplication table of a number multiplied 10 times (entered by user).
n = int(input("Enter a number : "))
for i in range (1,11):
    print (a,"x",i,"=",i*n)


# Question 3: Calculate the sum of all numbers from 1 to 100 using a for loop.
sum =0                             # intially sum ka value zero hai 
for i in range (1,101):
    sum +=i                        # sum = sum + i
print(sum)                         # Finally print is outside the loop it will print the final sum value.


# Question 4: Print the following pattern using a for loop:
#    *
#    **
#    ***
#    ****

for i in range(1,5):
    print("*"*i)

#-----------------------#----------------------#------------------#------------------#--------------------#------------------#---------------------#----------------------#-------------------#----------------------#


# TOPIC 4: WHILE LOOPS

# Practice Question 1: Print numbers from 1 to 10 using a while loop.

m = 1
while (m<=10) :
    print(m)
    m = m+1

# Practice Question 2:Write a program that keeps asking the user to enter a password until they enter the correct one.
# # OG IRL


Entered_pass=input("Enter your password : ")
Pass="Sanchal"
Attempt=5
while(Attempt>=1):
    if(Entered_pass == Pass):
        print("Password is correct, Authorization guaranteed")
    else:
        print("Password is incorrect, u have",Attempt,"attempts left")
        Entered_pass=input("Enter your password :")
    Attempt= Attempt - 1
    if(Attempt==1):
        print("This is your last chance to Login X")

#-----------------------#----------------------#------------------#------------------#--------------------#------------------#---------------------#----------------------#-------------------#----------------------#


# Topic 5 : Break, Continue and Pass

# Question 1: Use a for loop to print numbers from 1 to 10, but stop the loop if the number is 7 (use break).

for i in range (1,11):
    print(i)
    if (i==7):
        break


# Question 2: Print numbers from 1 to 10, skipping the number 5 (continue)
for i in range (1,11):
    if (i ==5):
        continue
    print(i)


# Question 3:Write a loop that goes through numbers 1 to 5, but does nothing for number 3 (use pass).
for i in range (1,6):
    match i:
        case 1:
            print(1)
        case 2:
            print(2)
        case 3:
           pass
        case 4:
            print(4)
        case 5:
            print(5)

#-----------------------#----------------------#------------------#------------------#--------------------#------------------#---------------------#----------------------#-------------------#----------------------#




    


