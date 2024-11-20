from Car import Car

newCode = "--------------------------------------------"

car = Car("Chevy", "Silverado", 2014, "Midnight-Black")
car1 = Car("Ford", "Mustang", 2012, "Cherry-Red")

print(car.make)
print(car.model)
print(car.year)
print(car.color)
car.drive()
car.stop()
print(newCode)

print(car1.make)
print(car1.model)
print(car1.year)
print(car1.color)
car1.drive()
car1.stop()
print(newCode)