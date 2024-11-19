import os

source = "copy.txt"
destination = "C:\\Users\\PC\\Desktop\\copy.text"

try :
    if os.path.exists(destination) :
        print("There is already a file there!")
    else :
        os.replace(source, destination)
        print(source + " was moved!")

except FileNotFoundError :
    print(source + " was not found!")