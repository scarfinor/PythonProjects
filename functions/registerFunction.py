# function = a block of code which is executed only when it is called. (invoked)

space = " "
newCode = "--------------------------------"

def hello(name) :
    print("Hello, " + name)

hello("Richard")
print(newCode)

name = "Ryan"
hello(name)
print(newCode)

def formalHello(firstName, lastName) :
    print("Hello, " + firstName + space + lastName)


formalHello("Richard", "Scarfino")
print(newCode)

def register(firstName, lastName, age, email) :
    print("Name: " + firstName + space + lastName + "\nAge: " + str(age) + "\nEmail: " + email)

register("Richard", "Scarfino", 29, "test@gmail.com")
print(newCode)