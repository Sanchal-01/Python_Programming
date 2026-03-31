# The Break statement is used to exit a loop prematurely.

for i in range (1, 10):
    if i == 7:
        break   # when i == 7 STOP the execution of the loop completely and exit the loop. Do not execute anything below break inside the loop. 
    print(i)
print("\n")   



for l in range (15, 25):
    if (l < 19):            # When l == 19, "if"  condition becomes false and else condition executes. "Note" : Else koi loop nahi hai wo bas if ka alternative hai.
        print(l)            
    else:                   # Where there's a break statement which forces to get out of the loop completely and do not check for next conditions anymore. like when l=20/21/22 
        break


# Practice Question 1 : Determine O/P
for i in range(1, 6):
    if i == 3:
        break
    print(i)


# Practice Question 2 : Determine O/P
for i in range(1, 6):
    print(i)
    if i == 3:
        break
    print("Hello")

# Practice Question 3 : Determine O/P
for i in range(1, 6):
    if i == 2:
        continue
    if i == 4:
        break
    print(i)

#  Practice Question 4 : Determine O/P
for i in range(0,3):
    for j in range(0,3):
        if j == 1:
            break
        print(i, j)



# Important Question 1 :
# Write a program which loop 1 to 50, if number divisible by 3 -->skip,if number divisible by 7--> STOP. Print rest of the numbers.

for i in range (1,51):
    if (i% 3== 0):
        continue
    if (i% 7 ==0):
        break
    print(i)



# Important Question 2:  Write a program

# Task:Loop from 1 to 20
# - If the number is even → print "Even",
# - If the number is odd → print the number itself,
# - If the number is 13 → stop the loop completely,

for m in range (1, 21):
    if(m==13):
        break
    if (m %2 ==0):
        print("Number is Even")
    else:
        print("Odd number is = ",m)
    
  

