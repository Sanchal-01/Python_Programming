# Writing to a file : Given  the name of the file 

# Whenever we commit something to a pre-existing file in write mode, the earlier content of the file would be overwritten and the new 
# give content would completely replace the old content. 
# That is we overrite the pre-exisiting data.


f = open("Henry.txt" , "w")

String ='''
This side Henry, I love playong video games and cricket as well.
I have developed multiple games. 
I am a game developer.
''' 
f.write(String)

print("The write operation executed successfully.......")

f.close()