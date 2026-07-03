# Convert string to integer
num_str = "10"
num_int = int(num_str)
print(num_int,"&", type(num_int))              # Output: 10



# Converting integer to string
num = 25
num_str = str(num)
print(num_str, "&", type(num_str))             # Output: "25"


# Converting float to integer
pi = 3.14
pi_int = int(pi)
print(pi_int, "&", type(pi_int))               # Output: 3


# Self created and solved example of typecasting 
My_name= "Sanchal"
My_age="22"
c=int(My_age)
print(c, "&", type(c) )


# NOTE: int() -------> sirf numbers ko convert karta hai integer value mein, text ko nahi. 
# g = int("sanchal")
# print(g, type(g))     # This would cause an error as Invalid Literal for int()

# Same goes with other data types i.e.if suppose kisi variable mein Integer value stored hai to hum use string bana 
# sakte hain but characters generate nahi kara sakte.