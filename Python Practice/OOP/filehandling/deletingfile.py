# deleting file using python

import os
import shutil

files = "test.txt"

try:
    #os.remove(files) #for file
    #os.rmdir(files)  #for directory
    #shutil.rmtree(files) # be carefull using this function this can function can delete all directory
    print(files+" file was deleted!")
except FileNotFoundError:
    print("That file was not found")
except PermissionError:
    print("You do not have permission to delete that")
except OSError:
    print("You cannot delete that using that function")
else:
    print(files+" was dleted")