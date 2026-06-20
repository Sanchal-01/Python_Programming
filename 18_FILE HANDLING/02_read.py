f = open("Sanchal.txt", "r" )   # Here f is a file object = Open (File name , mode)

# Here r = read & t = text file ====> "rt" = read text file. It is not necessary to write rt, just "r" would work fine as well sice "t" is default.
# Also we can use "rb" for reading binary files as well.

content = f.read()    # This means read the file and store the content inside 'content' variable.

print(content, "\n")

f.close()      # close function is used to flush and close the file.

#----------------------------------------------------------------------------------------------------------------------------------------------------

# This is a example of how we can resolve the situation when the file is missing by any chance.

try:
    file = open("Sanchal.txt", "r")  # Open in read mode
    content = file.read()  # Read the entire file content
    print(content, "\n")
    file.close()  # Close the file
except FileNotFoundError:
    print("File not found.")

#----------------------------------------------------------------------------------------------------------------------------------------------------