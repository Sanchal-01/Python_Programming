# Python’s os module provides functions are used for interacting with the operating system such as working with directories and files.

import os

a = os.listdir("18_FILE HANDLING\DIRECTORY")
print(a)

# This getcwd(): [Get the name of Current Working Directory] is used to find out in which directory we are currently working in :
print(os.getcwd())

# This command os.path.exists() is used to check whether the particular directory exists or not
# exists: True 
# does not exists :False
print(os.path.exists("18_FILE HANDLING\DIRECTORY"))


# For removing a File inside a directory:
os.remove("18_FILE HANDLING/DIRECTORY/sammy.txt")
print("The file is removed successfully......")

# Foe removing the entire directory: It only deleted the directory if it's completely empty:
os.rmdir("18_FILE HANDLING\DIRECTORY")  # O/P :The directory is not empty: '18_FILE HANDLING\\DIRECTORY'