# Most Common GitHub API URLs

# User Info
'''https://api.github.com/users/Sanchal-01'''

# Repositories
'''https://api.github.com/users/Sanchal-01/repos'''

# Public Events
'''https://api.github.com/users/Sanchal-01/events'''

# Followers
'''https://api.github.com/users/Sanchal-01/followers'''

# Following
'''https://api.github.com/users/Sanchal-01/following'''

#-----------------------------------------------------------#-----------------------------------------------------------#-----------------------------------------------------------#
# Requests is an elegant and simple HTTP library for Python, built for human beings.
# This Python requests module lets us send HTTP requests to websites and web APIs using code. 
# It acts like a web browser but operates completely inside our Python script.


import requests 
import json

# USER : Hey requests go and fetch the content of this url.
# REQUEST : I will do that and it will make a simple get requests to get the content of this url.

response = requests.get('https://api.github.com/users/Sanchal-01')

# (response.text)  # This will print the fetched content from the url in the form of text.




# 2. Creating a new file for storing the fetched content in the form of text;

with open("19_WORKING _with_EXT_LIBRARIES/Sanchal-01.txt", "w") as f:
    f.write(response.text)                    #  Plain string  
print("File created and data stored successfully.......")



# 3. If we want to se the response in a vertical manner we can also do that :

response = requests.get("https://api.github.com/users/Sanchal-01")   #

data = response.json()   # Python dictionary 

with open("19_WORKING _with_EXT_LIBRARIES/Sanchal-01.txt", "w") as file:
    json.dump(data, file, indent=4)


# json.dump()    Writes JSON to a file  
# json.dumps()   Converts JSON to a formatted string 
# indent=4       Makes JSON pretty and readable 


