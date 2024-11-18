capitals = {"USA" : "Las Vegas",
            "India" : "New Dehli",
            "China" : "Beijing",
            "Russia" : "Moscow"}

capitals.update({"Italy" : "Rome"})
capitals.update({"USA" : "Washington DC"})
capitals.pop("China")

newCode = "-------------------------------"

print(capitals["Russia"])
print(newCode)
print(capitals.get("Germany"))
print(newCode)
print(capitals.get("Russia"))
print(newCode)
print(capitals.keys())
print(newCode)
print(capitals.values())
print(newCode)
print(capitals.items())
print(newCode)

for key, value in capitals.items() :
    print(key, value)
print(newCode)

capitals.clear()
print(capitals)
print(newCode)
