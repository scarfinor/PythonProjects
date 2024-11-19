import os
import shutil

filePath = "test.txt"
emptyFolderPath = "folder"
folderPath = "folder"
try :
    os.remove(filePath)
    os.rmdir(emptyFolderPath)
    shutil.rmtree(folderPath)
except FileNotFoundError :
    print("This file was not found")
except PermissionError :
    print("You do not have permission to delete that")
else :
    print(emptyFolderPath + " was deleted")
    print(folderPath) + " was deleted"