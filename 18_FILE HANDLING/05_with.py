# Working with 'with', is useful because there's no need to close the file after opening it 


with open("henry.txt", "r") as f:   # Here with is the context manager.
    content = f.read()
    print(content)
    # No need to write f.close() because file is already closed by default when using with syntax.


    