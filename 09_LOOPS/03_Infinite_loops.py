# Infinite loops: Be careful to avoid infinite loops by ensuring the conditions eventually becomes FALSE.

# Example: 
i = 1
while (i<5):
    print(i)
    # forgot to mention the increment here,
    # like i+= 1. Now this will go into an infinite loop and keep on printing 11111111111..........and system will eventually crash. 

# Intentionally we can trigger infinite loops
while True:
    print ("This will run forever")


# Always try to avoid such situations where either u not mention conditions for the loop/condition which make the loop go false.