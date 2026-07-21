# In Python, a while loop repeatedly executes a block of code as long as its condition fulfills to be True. 
# If the condition is False from the start, the loop body will not run even once because Python checks the condition before entering the loop.


# Infinite loops: Be careful to avoid infinite loops by ensuring the conditions eventually becomes FALSE.

# Example: 
i = 1
while (i<5):
    print(i)
    # forgot to mention the increment here,
    # like i+= 1. Now this will go into an infinite loop and keep on printing 11111111111..........and system will eventually crash. 


#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

# Using a Recursive Function : We can also create an infinite loop using a recursive function. Here is an example: "This I did after studying functions"
def infinite_print():
   print("This will print infinitely")
   infinite_print()
infinite_print()

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------#


# Intentionally we can trigger infinite loops:

# This way ensures that we assign while True condition to the loop and the code outside the while loop, below is also reachable:
value = True
while (value):
    print ("This will run forever")


while True:
    print ("This will run forever")


# Always try to avoid such situations where either u not mention conditions for the loop which make the loop go false.



#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------#


# Practical Use Cases

# Infinite loops are useful in various scenarios, such as:
# Servers: Servers often run in an infinite loop to continuously listen for and handle client requests.
# Games: Game loops run indefinitely to keep the game running until the user decides to exit.
# Monitoring Systems: Systems that monitor resources or events continuously use infinite loops to stay active.