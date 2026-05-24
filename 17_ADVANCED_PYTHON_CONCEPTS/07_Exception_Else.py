# The else and Finally:
# else: The else block is optional and is executed only if no exception occured within the try block. Its useful for code that should run only when try block succeeds.



try :
    a = int(input("Enter the 1st number : "))
    b = int(input("Enter the 2nd number : "))
    print(f"The division is {a/b}.")

except Exception as e:
    print(f"{e}")

# Gets executed when there is no error in try block:
else:
    print("Everything is good to go........")




while True:
    try:
        file = open("test.txt", "r")
        content = file.read()
    except FileNotFoundError:
        print("File not found!")
    else:
        print("File read successfully.")
        print(f"File contents:\n {content}")
