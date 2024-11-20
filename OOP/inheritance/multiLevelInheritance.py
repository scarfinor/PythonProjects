newCode = "------------------------------"

class Organism :
    alive = True

class Animal(Organism) :
    def eat(self) :
        print("This animal is eating")

class Dog(Animal) :
    def bark(self) :
        print("This dog is barking")

dog = Dog()
print(dog.alive)
print(newCode)
dog.eat()
print(newCode)
dog.bark()
print(newCode)
