name = "Sanchal_020101990"
# name  = S a n c h a l
# index = 0 1 2 3 4 5 6

print (name[0:4])        # The index slicing  goes from 0 to (4-1) i.e., 3 
print (name[0:7])        # This goes from 0 to 6(7-1):Sanchal.



# CONCEPT: Printing with skipping characters

# print (name[0:10:n])   # Skip (n - 1) characters.
print (name[0:12:1])     # Skip 0 character.
print (name[0:12:3])     # Skip (3 - 1) ie 2 characters.



# CONCEPT: Printing without mentioning start/end of slicing

print (name[:5])         # Repalace the first empty number  with 0 # name[0:5]
print (name[1:])         # Replace the second empty number with length # name[1:17]



# CONCEPT: Reversing a string

print(name[17::-1])        # Output: 099101020_lahcnaS  (reverses string)

