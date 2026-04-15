# Functions help in reusability and modularity in Python.
# NOTE : 👉 print() kuch return nahi karta 👉 iska return value = "None"

a = 2
b = 3
c = 4
average = (a +b +c)/3
print("Average value(without function) = ",average)
print("\n")

# Printing Average Value by using functions:

def average(a, b, c):
    operation = (a+b+c)/3
    print("Average value = ",operation)  # print() sirf output show karta hai, koi useful value return nahi karta. 

# Call function (sirf display ke liye)
average(2, 4, 4)    # Yaha pe average function ve ander parameters ko value pass ki.

Value_1 = average(2, 4, 4)  
print("Average value (using print):",Value_1)  # Isliye agar hum print() ko kisi variable mein assign karte hain, to us variable ki value "None" ho jaati hai.
print("\n")


#-----------------------#----------------------#------------------#------------------#--------------------#------------------#---------------------#

def average_2(d, e, f):
    operation_2 = (d+e+f)/3
    return(operation_2)   # Agar hume value reuse karni hai, to function mein return() use karna chahiye.

# Call function   
average_2(1, 2, 3)

Value_2 = average_2(1, 2, 3)
print("Average value (using return):",Value_2)
print("\n")

#-----------------------#----------------------#------------------#------------------#--------------------#------------------#---------------------#

def greet(name):
    return(f"Hello, {name}!")

print(greet("Alice"))           # Output: Hello, Alice!