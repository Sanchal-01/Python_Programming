L_Number =int(input("Enter your Lottery ticket's last number : "))

    # Match case matches every I/P of user with eash case values, if satisfied/fulfilled --> the defined condition of that case is executed.
match L_Number:
    case 2:
        print("Better luck next time :)")

    case 5:
        print("Congrats you won a BMW car. Enjoy your trip.")

    case 4:
        print("Congratulations you won $3 million ")

    case _:   # Used as a default case when rest conditions are false/ unsatisfied.
        print ("No worries : Have a peaceful life ahead.")


#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
# Improvd version : We have introduced a try and except block here to handle critical conditons in case of user input is out of range.

while True:

    try:    
        user_input = input("Enter your Lottery ticket's last number : ").strip()  # Strip() is used to remove any whitespaces(leading or trailing) for the user input.

        if len(user_input) != 1 or not user_input.isdigit():
            raise ValueError


        L_Number = int(user_input)

        # Match case matches every I/P of user with each case values, if satisfied/fulfilled --> the defined condition of that case is executed.        
        match L_Number:
            case 2:
                print("Better luck next time :)")

            case 5:
                print("Congrats you won a BMW car. Enjoy your trip.")

            case 4:
                print("Congratulations you won $3 million ")

            case _:   # Used as a default case when rest conditions are false/ unsatisfied.
                print ("No worries : Have a peaceful life ahead.")

    except Exception as e:
        print("Invalid input. Please enter a single last_digit of your ticket.\n")