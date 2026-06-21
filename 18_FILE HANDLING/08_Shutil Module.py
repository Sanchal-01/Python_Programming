# ============================================================
# SHUTIL MODULE IN PYTHON
# ============================================================
#
# shutil (Shell Utility) module provides high-level file and directory operations such as:
#
# 1. Copying files
# 2. Moving files
# 3. Renaming files
# 4. Removing directories
# 5. Copying entire directory trees
#
# It is more powerful than basic file handling operations.
#
# Documentation for shutil(Advanced File Handling Operation) where I visited https://docs.python.org/3/library/shutil.html
# =======================================================================================

import shutil

shutil.rmtree ("DIRECTORY")
shutil.copy("sanchal.txt", "sanju.txt")


shutil.move("sanju.txt", "DIRECTORY/")

#---------------------------------------------------------------#---------------------------------------------------------------#---------------------------------------------------------------
# EXPLANATION:

import shutil

# ------------------------------------------------------------
# rmtree(): Removes an entire directory and all of its contents.

# WARNING:
# This operation is PERMANENT. Files and folders inside the directory will be deleted.

# Example:

# DIRECTORY/
# ├── file1.txt
# ├── file2.txt

# After rmtree(): DIRECTORY  --> Deleted completely

shutil.rmtree("DIRECTORY")




# copy(): Creates a copy of a file.
# ----------------------------------

# Syntax: shutil.copy(source, destination)
# Example:sanchal.txt becomes sanju.txt
# Original file remains unchanged.

# After operation:
# sanchal.txt
# sanju.txt
# Both files exist.

shutil.copy("Henry.txt", "18_FILE HANDLING\DIRECTORY")

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


# move()
# -------------------------------------------

# Moves a file from one location to another.
# Syntax: shutil.move(source, destination)
# If destination is a folder, the file is moved into that folder.

# Example:
# Before:
# DIRECTORY/
# sanju.txt


# After:
# DIRECTORY/
# └── sanju.txt
#
# The original file disappears from its old location.

shutil.move("sanju.txt", "DIRECTORY/")