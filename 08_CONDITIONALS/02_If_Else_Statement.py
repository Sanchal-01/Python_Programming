Promise =int(input("If you want to make a promise type 1 otherwise 0 :  ")) 

if(Promise==1):
    print("You are Eligible for the trip")
else:
    print("You are Not eligible for the trip \n")


if (Promise == 1):
    print ("The vacation has started.")
else:
    print("The vacation has ended before starting.")

#----------------------------------------------------------------------------------------------------------------------------------------------#

# More optimized way we have : 
# We have introduced exception handling below to deal with any critical situations where the user inputs values other than 0 or 1.

while True :

    try:
        Promise = int(input("If you want to make a promise type 1 otherwise 0 :  "))

        if (Promise == 1):
            print("You are eligible for the trip and the vactaion has started.")

        else:
            print("You are not eligible for the vacation and sadly the trip has ended.")

    except Exception as e:
        print("Please enter the input as 0 or 1",e)
