n = 5
for i in range (1,n):
    print ("Hello! How are u ??")

# Here the for loop works within a range of values where, range is from 1 to (n-1) i.e. 4. That's why print function prints values from 1 to 4, that is 4 times iteration.


# METHOD : 1
for l in range(1, 5):
    print (l)
print("\n")

# METHOD : 2
for l in range(1, 5):
    print (l)
    print("\n")

# Both Method 1 and Method 2 looks similar at first but are actually different.

# CONCEPT of for loop for METHOD 1: Here the start= 1, end= 4 i.e., for loop will iterate(run in a cycle) 4 times.
# During the 1st iteration the functions written inside the for loop will get executed line by line i.e. print (1)
# During the 2nd iteration the functions written inside the for loop will get executed line by line i.e. print (2)
# During the 3rd iteration the functions written inside the for loop will get executed line by line i.e. print (3)
# During the 4th iteration the functions written inside the for loop will get executed line by line i.e. print (4)
# Now the for loop execution is complete. Get out of the loop.
# "Break the line". This will happen only once after the for loop iteration is complete as "\n" is written outside the for loop.

# CONCEPT of for loop for METHOD 2: Here the start= 1, end= 4 i.e., for loop will iterate(run in a cycle) 4 times.
# The only change this Method has form M1 is that the 'print' function is 'inside' the for loop.
# Due to which during the 1st iteration the functions written inside the for loop will get executed line by line i.e. print (1) next print("\n").
# During the 2nd iteration the functions written inside the for loop will get executed line by line i.e. print (2) next print("\n").
# Thus "Break the line" (escape sequen opr) will be called durint every iteration as it is written inside the for loop.



for k in range(6):
    print(k)
# By default the start value  is inclusive(i.e. if not mentioned it's 0) and the end is 5(6-1) as I have written above.



for i in range (1, 6):
    print("Blessings of our elders are always with us.")
    print("SO, don't worry :) ")                            # Removed this print statement out of the second loop to ensure that it is not printed after the completion of !st loop containing i as iterator.

#-----------------------------------------------------------#-----------------------------------------------------------#-----------------------------------------------------------#
# Another way of solving the above problem statement: 

for i in range (1, 6):
    print("Blessings of our elders are always with us.")
    for j in range(1):                                     # This static 1 ensures that the loop is executed only once aafter the first for loop.
            print ("No need to worry about anything.")

#-----------------------------------------------------------#-----------------------------------------------------------#-----------------------------------------------------------#

# Table of 7 :
for m in range(1, 16): # Value of m(i.e. 5 x m) starting from 1 goes to 15.
    print("7","X",m,"=",7*(m))



# Allowed user to enter the number of their choise for table creation : 
user_input = int(input("Enter number whose table you want to have: "))
for i in range (1, 11):
     print(f" {user_input} X {i} = {user_input * i}")
     