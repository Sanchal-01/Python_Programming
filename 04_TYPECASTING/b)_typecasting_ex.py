# Convert string to integer
num_str = "10"
num_int = int(num_str)
print(num_int)              # Output: 10
print (type(num_int))


# Convert integer to string
num = 25
num_str = str(num)
print(num_str)             # Output: "25"
print(type(num_str))


# Convert float to integer
pi = 3.14
pi_int = int(pi)
print(pi_int)               # Output: 3
print(type(pi_int))


# Self created and solved example of typecasting 
My_name= "Sanchal"
My_age="22"
c=int(My_age)
print(c)
print(type(c))

# NOTE: int() → sirf numbers ko convert karta hai integer value mein, text ko nahi.Same goes with other data types i.e.
#if suppose kisi variable mein Integer value stores hai to hum use string bana sakte hain but characters generate nahi kara sakte.