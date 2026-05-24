# finally : The finally block is also optional and is always executed --> regardless of any error occured or not.
# file.close() :Its typically used for cleanup opertions,such as CLOSING files or Releasing resources.



while True:
    try:
        a = int(input("Enter the first number: "))
        b = int(input("Enter the second number: "))
        print(f"Division = {a/b}")

    except Exception as e:
        print(f"{e}")

    finally:
        print("This is always executed no matter error occured or not")





while True:
    try:
        file = open("test.txt", "r")
        content = file.read()
    except FileNotFoundError:
        print("File not found!")
    else:
        print("File read successfully.")
        print(f"File contents:\n{content}")

    finally:
        file.close()     # Ensures the file is closed no matter what