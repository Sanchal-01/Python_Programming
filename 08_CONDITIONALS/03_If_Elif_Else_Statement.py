# Scenario: India scored 198 runs in the fianls against New Zealand. New Zealand needs 199 runs to win this match.
# Design a program which can cover all the scenarios of which team will win and which won't.

score = int(input("Enter the expected score here : "))

if(score>198):
    print("India will win this match")
elif(score == 198):
    print("It's a draw, we shall have a super over. ")
else:
    print("New Zealand will win this match")


#---------------------------------------------------------------------------------------------------------------------------------------------#

try:
    score = int(input("Enter the expected score here : "))

    if(score>198):
        print("India will win this match")
    elif(score == 198):
        print("It's a draw, we shall have a super over. ")
    else:
        print("New Zealand will win this match")

except Exception as e:
    print ("Input integer values only",e)