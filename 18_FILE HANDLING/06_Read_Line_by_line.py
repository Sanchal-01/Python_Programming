# Reading line by line ensures that new line is well separated from previous line and it ensures readability and the database is getting populated line by line.

try:
    f = open("Henry.txt", "r")
    for line in f:
        # content = f.read()  This shouldn't be written because it reads the entire content at once instead of line by line.
        print(line)
    f.close()
except:
    print("File not found.")

#-------------------------------------------#-------------------------------------------#-------------------------------------------#-------------------------------------------

# Anoter way of improving readability is to put 'line.strip()' to remove "\n" at the end to every line.
# strip() removes leading and trailing whitespace.
# Most importantly here, it removes '\n from the end of each line. Example:
# "Hello\n"  ->  "Hello"
# "Python\n" ->  "Python"

try:
    file = open("Sanchal.txt", "r")
    for line in file: # Efficient for large files
        print(line.strip()) # Remove newline characters
    file.close()
except FileNotFoundError:
    print("File not found.")

#-------------------------------#-------------------------------#-------------------------------#-------------------------------#-------------------------------
# ============================================================
# QUICK INTERVIEW NOTE
# ============================================================

# f.read()
# ----------
# Reads entire file at once.
# Best for:  Small files.


# for line in file
# ----------------
# Reads one line at a time.
# Best for: Large files.


# line.strip()
# ------------
# Removes whitespace and '\n' from both ends of a string.


# with open(...)
# --------------
# Recommended way to work with files because Python automatically closes the file.