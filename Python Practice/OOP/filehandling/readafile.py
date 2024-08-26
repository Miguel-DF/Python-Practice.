# base case for file handling
try:
    #execute if file is true
    with open('file.txt') as file:
          print(file.read())
    #execute if file doesn't exist
except FileNotFoundError:
    print("file not found")