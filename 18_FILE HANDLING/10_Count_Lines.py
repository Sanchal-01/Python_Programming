import sys

def count_lines(filename):
     with open(filename, "r") as f:
          return len(f.readlines())
     
if __name__ == "__main__":
     filename = sys.argv[1]
     num_lines = count_lines(filename)
     print(f"There are {num_lines} lines in {filename} ")


# Terminal : 
# python '.\18_FILE HANDLING\10_Count_Lines.py' '.\18_FILE HANDLING\DIRECTORY\Henry.txt'