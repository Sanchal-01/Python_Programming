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