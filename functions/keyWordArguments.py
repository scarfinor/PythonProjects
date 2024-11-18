# keyWord arguments = arguments preceded by an identifier when we pass them to a function. the order of the arguments doesn't matter.

space = " "

def formalHello(firstName, middelName, lastName) :
    print("Hello, " + firstName + space + middelName + space + lastName + "!")

formalHello(lastName = "Scarfino", middelName = "Rosario", firstName = "Richard")