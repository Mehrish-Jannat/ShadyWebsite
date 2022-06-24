class Car:
    def __init__(self,colour,brand,doors):
        self.colour = colour
        self.brand = brand
        self.doors = doors
    def start(self):
        print("Crash")


car1 = Car("yellow","audi",4)
print(car1.colour)
print(car1.doors)
car1.start()
        