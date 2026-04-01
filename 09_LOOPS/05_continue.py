# continue is a loop control statement.
# The continue statement skips the code in the current iteration and moves to the next iteration.

# Example 
for i in range(1, 10):
    if (i==6):   # During the 6th iteration when i is equal to 6, continue was executed, so the current iteration is skipped and 6 is not printed.
        continue
    print(i)



# Example
for i in range (10):
    if i==(4):   # The 4th iteration was skipped just because of continue.
        continue
    print (i,"It's okay!!")




