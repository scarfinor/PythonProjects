text = "This is how you can write a new file in Python!"
append = "\nThis is how you can append a file in Python!"


# Write a new file
with open("test.txt", "w") as file :
    file.write(text)

#Append an existing file
#with open("test.txt", "a") as file :
#   file.write(append)

with open("test.txt", "r") as file :
 print(file.read())