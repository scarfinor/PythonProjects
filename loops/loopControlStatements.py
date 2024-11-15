from loops.types import newCode, newConcept

while True :
    name = input("Enter your name: ")
    if name != "" :
        break

print(newCode)

phoneNumber = "123-456-7890"

for i in phoneNumber :
    if i == "-" :
        continue
        print(i, end = "")