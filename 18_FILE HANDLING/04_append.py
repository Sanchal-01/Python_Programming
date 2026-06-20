# Appending to a file : Given the name of the pre- existing file.
# If the file does not exists then new file would be created with that name.

# Whenever we commit something to a pre-existing file in append mode, the earlier content of the file would stay intact and
# the new given content would be added next to the old content. 
# That is we add the new content at the last of the existing content.

f = open("Henry.txt" , "a")

String ='''
Henry is a very nice guy.
2 years ago he was living in California, USA.
''' 
f.write(String)

f.close()