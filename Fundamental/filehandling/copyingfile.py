#copyfile() = copies contents of file
#copy() = copyfile() + permission mode + destination can be a directory
# copy2() = copy() + copies metadata (file's creation and modification times)

import shutil

shutil.copyfile('copy.txt','test.txt') #source.destination

