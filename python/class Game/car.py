class Car:
    def __init__(self, weight: int, topSpeed: int, awd: bool, horsepower: int) -> None:
        self.weight = weight
        self.topS = topSpeed
        self.awd = awd
        self.power = horsepower


    def accelerate(self):
        print('moving')

    def brake(self):
        print('stopping')

    def reverse(self):
        print('backing up')
#-----------------------------------------------------------------------------------------------------------------
class eCar(Car):
    def __init__(self, weight: int, topSpeed: int, awd: bool, horsepower: int, battery: int) -> None:
        self.battery = battery
        self.range = battery * 2
        super().__init__(weight, topSpeed, awd, horsepower)

    def charging(self):
        print('charging')
#-----------------------------------------------------------------------------------------------------------------
class iceCar(Car):
    def __init__(self, weight: int, topSpeed: int, awd: bool, horsepower: int, tank: int) -> None:
        self.tank = tank
        super().__init__(weight, topSpeed, awd, horsepower)

    def fueling(self):
        print('fueling')
#-----------------------------------------------------------------------------------------------------------------

car = iceCar(100,100,True,100,100) 
car.accelerate()
car.brake()
car.reverse()
car.fueling()
print(car.tank)

