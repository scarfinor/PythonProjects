# str.format() = optional method that gives users more control when displaying output.

num = 1000

print("The number pi is {:.3f}".format(num)) # display first two digits after decimal
print("The number pi is {:,}".format(num)) # add "," to all 1,000 place
print("The number pi is {:b}".format(num)) # display binary representation of the number
print("The number pi is {:o}".format(num)) # display octal number
print("The number pi is {:x}".format(num)) # display hexadecimal number
print("The number pi is {:e}".format(num)) # display scientific notation