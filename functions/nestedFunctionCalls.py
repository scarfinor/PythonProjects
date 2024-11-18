# nested function calls = function calls inside other function calls innermost function calls are resolved first the returned value is then used as the argument for the next outer function.

newCode = "---------------------------------------"

num = input("Enter a whole positive number: ")
num = float(num)
num = abs(num)
num = round(num)
print(num)
print(newCode)

print(round(abs(float(input("Enter a whole positive number: ")))))
print(newCode)
