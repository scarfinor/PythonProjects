class Car :

    def __init__(self , make, model, year, color) :
        self.make = make
        self.model = model
        self.year = year
        self.color = color

    def drive(self) :
        if self.model == "Silverado":
            print("You start the truck and begin to drive.")
        else:
            print("You start the car and begin to drive.")

    def stop(self) :
        if self.model == "Silverado" :
            print("You turn of the truck and get out.")
        else :
            print("You turn of the car and get out.")