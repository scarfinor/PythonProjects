# exception = events detected during execution that interrupt the flow of a program

space = " "

try :
    numerator = int(input("Enter a number to divide: "))
    denominator = int(input("Enter a number to divide by: "))
    result = numerator / denominator
except ZeroDivisionError as e :
    print(e)
    print("You can't divide by zero!")
except ValueError as e :
    print(e)
    print("Enter only numbers please")
except Exception as e :
    print(e)
    print("there was an unknown exception!")
else :
    print(result)
finally :
    print(numerator + space + "is divisible by: " + denominator)