# To modify a global variable inside a function, use the global keyword:

x = 10    # Global variable x

def modify_global():
    global x               # Please Modifiy the global x to x = 5
    x = 5                 # This will refer global variable to x = 5.
    print(x)

modify_global()

print("Global x =",x)      # Here the value of x global is ?




z = 40   # Global Variable z

def sum(a, b): 
    global z              # Please Modifiy the global z to z = 5
    z = 10
    return (a + b + z)
print("Sum of three numbers is",sum(2,3))

print("Global z = ",z)    # Here the value of z global is ?