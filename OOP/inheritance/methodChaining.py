# method chaining = calling multiple methods sequentially. Each call preforms an action on the same object and returns self

class Car :
    def turnOn(self) :
        print("The car turns on")
        return self

    def drive(self) :
        print("The car is driving")
        return self

    def brake(self) :
        print("The car applies the brakes")
        return self

    def turnOff(self) :
        print("The car turns off")

car = Car()

car.turnOn().drive().brake().turnOff()