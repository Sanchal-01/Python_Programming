# WHAT IS A MODULE IN PYHTON?
# In Python, a module is a file containing Python definitions and statements. It allows you to logically organize your code by grouping related functions, classes, and variables into a single file with a .py extension.

# Python provides built-in and third-party modules
# - Built in Module 
# - External Module


# 1. Built in Module :

import math
print (math.sqrt(25))

import os
# print(os.abort())   # Iske baad ka code kabhi execute hi nahi hota.

# If any module is unused it looks slight different.
# List of all the built in modules in python: https://docs.python.org/3/py-modindex.html 



# 2. Third Party or External Modules : 
import mymodule
print(mymodule.hello("Sanchal"))


# Installing external Modules :
# pip install requests 
# pip install pandas 

import requests

response = requests.get("https://api.github.com")
print(response.status_code)