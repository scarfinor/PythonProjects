from locale import locale_alias

newCode = "--------------------"

while True :
    name = input("Enter your name: ")
    if name != "" :
       break

print(newCode)

phoneNumber = "123-456-7890"
stop = " "

for i in phoneNumber :
    if i == "-" :
        continue
    print(i, end="")
print(stop)

print(newCode)

for i in range (1, 5) :
    if i == 3 :
        pass
    else:
        print(i, end="")
print(stop)

print("====================")