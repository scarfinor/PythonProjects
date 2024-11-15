import time

newCode = "----------------"
newConcept = "================"

for i in range(10) :
    print(i + 1)

print(newCode)

for i in range(50, 100 + 1) :
    print(i)

print(newCode)

for i in range(50, 100, 2) :
    print(i)

print(newCode)

for i in range(50, 101) :
    print(i)

print(newCode)

for i in "Richard Scarfino" :
    print(i)

print(newCode)

for seconds in range(10, 0, -1) :
    print(seconds)
    time.sleep(1)

print("this is a countdown timer!")

print(newConcept)

name = ""

while  len(name) == 0 :
    name = input("Enter your name: ")
print("Hello, " + name)

print(newCode)

name = None

while not name :
    name = input("Enter your name: ")
print("Hello, " + name)

print(newConcept)