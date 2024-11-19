try :
    with open("C:\\Users\\PC\\Desktop\\dev tools Lc101\\zopener_8a4800ea0a3f43f4bafd7706c1a4e7ee.log") as file :
     print(file.read())
except FileNotFoundError :
    print("This file was not found!")
print("------------------------------")
print(file.closed)