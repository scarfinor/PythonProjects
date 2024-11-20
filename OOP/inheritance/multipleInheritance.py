# multiple inheritance = a child class is derived from more than one parent class

newCode = "---------------------------"

class Prey :
    def flee(self) :
        return print("This animal flees")

class Predator :
    def hunt(self) :
        return print("This animal hunts")

class Rabbit(Prey) :
    pass

class Hawk(Predator) :
    pass

class Fish(Prey, Predator) :
    pass

rabbit = Rabbit()
hawk = Hawk()
fish = Fish()

rabbit.flee()
print(newCode)
hawk.hunt()
print(newCode)
fish.flee()
fish.hunt()
print(newCode)

