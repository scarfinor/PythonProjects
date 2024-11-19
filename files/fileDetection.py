import os

path = "C:\\Users\\PC\\Desktop\\dev tools Lc101\\zopener_8a4800ea0a3f43f4bafd7706c1a4e7ee.log"

if os.path.exists(path) :
    print("This location exists!")
    if os.path.isfile(path) :
        print("This location a file!")
    elif os.path.isdir(path) :
        print("This location a file directory!")
else:
    print("This location doesn't exist!")