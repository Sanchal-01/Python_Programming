# 1. Write a program to print : Hello, World! Welcome to Python.
print("Hello, World! Welcome to Python.")

# 2. Write a program that prints poem using a single print statement:
print("Twinke, twinke, little star,\nHow I wonder what you are!!")

# 3. Create a varible to store: Your (name), Your(age), Your(Height in meters),
# A boolean value representing whether you are a student/not:
My_name ="Sanchal Kumar"
My_Age = 21
My_Height = (169,"cm")

if(My_Age>=21):
    print (True,"Student")
else:
    print(False)

# 4. You are given a string num="45".Convert it into an integer, Add 10 to it & Print the result.
num="45"
int_num=int(num)
int_num +=10
print(int_num)

#OR
integer = int("45")
integer += 10
print(integer)


# 5. Write a program that:
# Asks user for their favourite food and prints Wow!I also like <food>.
food=input("Enter the name of your favourite food here : ")
print("Are u serious! Wow! I also like,",food)


# 6. Write a program that takes 2 numbers as input from the user :
# prints their >sum, >difference, >Product, >Quotient.
num_1=int(input("Enter your 1st number : "))
num_2=int(input("Enter your second number : "))
sum= num_1 + num_2
diff= num_1 - num_2 
product= num_1* num_2
quotient= num_1/num_2
print(sum,diff,product,quotient, sep="\n")


# 7. Escape Sequence:Print the following output using escape sequences:
# Hello "Python" World!
# This is on a new line.
# This is a tab →	    after tab.
print("Hello \"Python\" World!\n""This is on a new line\n""This is a \t after tab")

# 8. Write a program that takes an integer as input from the user and prints the square & cube of that number.
a = int(input ("Enter a  number : "))
b =int(input ("Enter 2nd number : "))
a **= 2
b **= 3
print(a,b)