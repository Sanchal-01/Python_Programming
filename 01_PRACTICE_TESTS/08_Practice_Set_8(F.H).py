# FILE HANDLING and UTILITIES _ PRACTICE SET                                                                       22/06
# This set is based on the Topics we've covered so far :
# - File I/O in Python
# - Read, Write, Append Files
# - OS and Shutil Modules in Python
# - Creating Command Line Utilities


# TOPIC 1 : FILE I/O BASICS

# Q1. Create a text file notes.txt using Python and write "Learning Pyhton is fun!" into it.
f = open("01_PRACTICE_TESTS/notes.txt" , "w")

content = '''Learning Python is fun!!'''
f.write(content)
print("The content has been added successfully...")

f.close()


# Q2. Open notes.txt, read its content and print it to the console.
with open("01_PRACTICE_TESTS/notes.txt", "r") as f:
    content1 = f.read()
    print(content1)

print("\n","The file has been read successfully....")
f.close()

#-------------------------------------------------------------------------#-------------------------------------------------------------------------#-------------------------------------------------------------------------

# TOPIC 2 : Read, Write and Append Files 


# Q1. Write a python program that writes three lines of text to a file tasks.txt
with open("01_PRACTICE_TESTS/tasks.txt", "w") as file:
    content2 = '''
    My name is Sanchal 
    I like to code in Python 
    Python is a high level language.
    '''
    file.write(content2)

print("The file has been created with new content in it....")

file.close()


# Q2. Open tasks.tx in append mode and add a new line "Tasks Completed!!".
with open("01_PRACTICE_TESTS/tasks.txt", "a") as file2:
    content4 = '''Task Completed!! '''
    file2.write(content4)

print("File append Successful..")
file2.close()


# Q3. Read the file and print all the lines as a list using readlines().
with open("01_PRACTICE_TESTS/tasks.txt", "r") as file2 :
    for line in file2.readlines():
        print(line)
    

#-------------------------------------------------------------------------#-------------------------------------------------------------------------#-------------------------------------------------------------------------

# TOPIC 3 : OS and Shutil Modules

# Q1. Use the OS module to :

# Print the current working directory 
import os
d = os.getcwd()
print (d)

# List all file and folders in the directory
import os 
a = os.listdir()
print (a)


# Create a new folder my_folder
import os 
os.makedirs("01_PRACTICE_TESTS/OS_Modules")
print ("Folder creation successful...")


# Q2. Use the shutil Module to:

# Copy a file from one folder to another - 
import shutil
shutil.copy("01_PRACTICE_TESTS/notes.txt", "01_PRACTICE_TESTS/OS_Modules")
print("File copy Success....")


# Move a file to a new folder - 
import shutil
shutil.move("01_PRACTICE_TESTS/tasks.txt", "01_PRACTICE_TESTS/OS_Modules")
print("File has been moved...... :)")


# Delete a file (be careful : IRREVERSIBLE) - 
import shutil
shutil.rmtree("01_PRACTICE_TESTS/OS_Modules")
print ("File has been deleted.")

#-------------------------------------------------------------------------#-------------------------------------------------------------------------#-------------------------------------------------------------------------
