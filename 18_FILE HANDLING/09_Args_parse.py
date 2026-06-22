# When we want to design a program that will output sum of two number (eg 4 8 add) then this is where argparse shines.
# Whenever we want a command line utility i.e., a python program which can take inputs from the command line we can use something like:
# 
import argparse 

# Whenever we want to create a command_L_U we have to create a parser:

parser = argparse.ArgumentParser(description= "Human Calculator")

parser.add_argument("num1", type= float, help="First Number")   # help ensures what is shown in the command utility
parser.add_argument("num2", type= float, help="Second Number")

parser.add_argument("operation", choices= ["div", "mul", "add", "sub"], help= " Operation to Perform :")

args = parser.parse_args()

try:
    if(args.operation == "add"):
        print(f"The sum of {args.num1} & {args.num2} is {args.num1 + args.num2}.")

    elif(args.operation == "mul"):
        print(f"The multiplication of {args.num1} & {args.num2} is {args.num1 * args.num2}.")

    elif(args.operation == "div"):
        print(f"The division of {args.num1} & {args.num2} is {args.num1 / args.num2}.")

    else:
        print(f"The substraction of {args.num1} & {args.num2} is {args.num1 - args.num2}.")

except ZeroDivisionError as e:
    print("some error has occured restart the terminal and operate again.", e)



# To duplicate a line (Alt + Shift + Down Arrow Key)