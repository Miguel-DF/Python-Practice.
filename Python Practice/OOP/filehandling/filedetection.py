#  file detection using python


import os

source = "test.txt" # the source file want you move
destination = "C:\\Users\\megel\\OneDrive\\test.txt" # the destination of file want you to be moved


try:
    if os.path.exists(destination): # if case for file if already there
        print("There is already a file there")
    else:
        os.replace(source,destination) # else the file will be moved
        print(source +" was moved")
except FileNotFoundError:
    print(source + " was not found") # if file doesn't existed