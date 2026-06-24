# A requirements. txt file lists all the packages our proctect needs/ depends upon.
# This makes it easy to create the environment on another machine with the same versions of the packages.

#---------------------------------------------------#---------------------------------------------------#---------------------------------------------------#

# STEP 1. First we have to see how many libraries have been installed in our environment, fot that we write:
'''pip freeze'''  # This will show us the libraries and packages installed 




# STEP 2. Putting the list of packages all together inside a new file..."requirements.txt"
"""pip freeze > requirements.txt"""

# This is a terminal command, we are taking output of freeze and putting into requirements.txt
# This will create a new file and will put the required packages in that new file.


# We can also decide where & in which folder we want to crreate the req.txt file(in my case I did this way):
"""pip freeze > '.\19_WORKING _with_EXT_LIBRARIES\requirements.txt'"""



# STEP 3: Here we can install all the required packages from requirements.txt file into our venv all together:
'''pip install -r requirements.txt'''  # Installs packages from the file