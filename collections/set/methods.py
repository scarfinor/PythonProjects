utensils = {"fork", "spoon", "knife", "knife", "knife"}
dishes = {"bowl","plate","cup"}
newCode = "---------------------------"

utensils.add("napkin")
utensils.remove("fork")
utensils.clear()
utensils.update(dishes)

for i in utensils :
    print(i)
print(newCode)

dinnerTable = utensils.union(dishes)

for i in dinnerTable :
    print(i)
print(newCode)

utensils.add("knife")
print(utensils)
print(newCode)
print(utensils.difference(dishes))
print(utensils.intersection(dishes))