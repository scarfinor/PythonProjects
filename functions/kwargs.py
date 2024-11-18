# **kwargs = parameter that will pack all arguments into a dictionary so that a function can accept a varying amount of keyword arguments.



def formalHello(**names) :
    print("Hello", end=" ")
    for key, value in names.items() :
        print(value, end=" ")

formalHello(title="Mr.", firstName="Richard", middleName="Rosario", lastName="Scarfino")