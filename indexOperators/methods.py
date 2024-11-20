# index operator [] = gives access to a sequence's element (str, list, tuple)

name = "richard Scarfino!"
newCode = "----------------------------------"

if (name[0].islower()) :
    name = name.capitalize()
print(name)
print(newCode)

firstName = name[:7].upper()
lastName = name[8:].lower()
lastCharacter = name[-1]
print(firstName)
print(lastName)
print(newCode)
print(lastCharacter)
print(newCode)

