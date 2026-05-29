# WHAT IS WALRUS OPERATOR?

# Walrus Operator (:=) is used to:
# 1. Assign a value to a variable AND
# 2. Use that value immediately in a SINGLE expression.

# Syntax: variable := expression

# Example:
x = 10 # Normal assignment:
print(x)

# Walrus assignment:   
print(y := 20)

# Here:
# Step 1: Assign 20 to variable y
# Step 2: Immediately use/return y value

# =========================================================# =========================================================# =========================================================# =========================================================

# WHY IS IT CALLED WALRUS OPERATOR?  Symbol := It visually resembles a walrus face.

# =========================================================# =========================================================# =========================================================# =========================================================

# NORMAL ASSIGNMENT VS WALRUS OPERATOR:

# Normal assignment:
length = len([1,2,3])
if length > 2:
    print(length)


# Using Walrus Operator:
if (length := len([1,2,3])) > 2:
    print(length)


# Difference:
# = Only assigns value
# := Assigns value AND returns it immediately

# =========================================================# =========================================================# =========================================================# =========================================================

# ROLE OF PARENTHESES ():
# Parentheses are usually used with walrus operator to make expressions clearer.

# Example:
if (n := 15) > 10:
    print(n)


# Without parentheses:

# if n := 15 > 10:     This becomes confusing and may produce errors.

# Therefore Use:       (variable := value)


# =========================================================
# COMMON USE CASE 1 : CONDITIONS
# =========================================================

# Without Walrus:

number = int(input("Enter number: "))

if number > 10:
    print("Large Number")


# With Walrus:
if (number := int(input("Enter number: "))) > 10:
    print("Large Number")


# What happens?

# Step 1: Input is taken
# Step 2: Value stored in variable number
# Step 3: number immediately used in condition


# =========================================================
# COMMON USE CASE 2 : LOOPS
# =========================================================

# Without Walrus:

name = input("Enter name: ")

while name != "exit":
    print(name)

name = input("Enter name: ")



# With Walrus:

while (name := input("Enter name: ")) != "exit":     # Jabtak name 'exit' nahi hoga loop chalta rahega. Agar blank bhi enter kar diye to Condition False mani jayegi and loop se exit ho jayenge. 
    print(name)

# Advantage:
# Input statement written only once
# Cleaner code



# =========================================================
# COMMON USE CASE 3 : LIST COMPREHENSION
# =========================================================

# Example:

result = [square
    for i in range(10)
    if (square := i*i) > 10
]
print(result)

# Here:
# i*i computed once,
# stored inside square,
# immediately used in condition



# =========================================================
# FLOW OF EXECUTION
# =========================================================

# Example:
if (x := 5) > 2:
    print(x)


# Execution:
# x := 5 --> Assign 5 to x -----> Return value 5

# Compare:
# 5 > 2  -----> True ----> print(x)


# =========================================================# =========================================================# =========================================================# =========================================================

# ADVANTAGES OF WALRUS OPERATOR :

# 1. Reduces repeated calculations
# 2. Makes loops cleaner
# 3. Reduces extra lines of code
# 4. Useful in comprehensions
# 5. Improves readability (when used correctly)

# DISADVANTAGE: Overusing makes code confusing.bAvoid writing unnecessarily complex expressions.

# =========================================================# =========================================================# =========================================================# =========================================================

# FINAL DEFINITION
# Walrus Operator (:=) is used to assign values to variables as part of an expression, allowing assignment and usage in a single statement.

