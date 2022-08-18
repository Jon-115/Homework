import random

namesList = ['Alex', 'Bonnie', 'Colin', 
        'Danielle', 'Earl', 'Fiona', 'Gaston', 'Hermoine',
        'Idalia', 'Jose', 'Karl', 'Lisa', 'Martin', 'Nicole',
        'Owen', 'Phillippe', 'Rina', 'Shary', 'Tammy', 'Virginie',
        'Walter']

namesList = namesList[::-1]

locations = ['Honolulu', 'Miami', 'Atlanta', 'Charlotte', 'Boston', 'New York', 'D.C.', 'Baltimore', 
        'Cape Hatteras', 'Morehead', 'Wilmington', 'Savannah', 'Myrtle Beach']

count = 1

class Storms:
    def __init__(self, destination: str,travelSpeed:int, name:str) -> None:
        self.dest = destination
        self.vel = travelSpeed
        self.name = name

    count = 1
        
    def info(self):
        print("the name is "+ self.name)
        print("The destination is "+ self.dest)
        print("The travel speed is "+ str(self.vel))
        print("")

class cat5(Storms):
    def __init__(self, destination = "", travelSpeed = 100, name= "") -> None:
        name = namesList.pop()
        destination = locations[random.randint(0,len(locations)-1)]
        super().__init__(destination, travelSpeed, name)

class cat4(Storms):
    def __init__(self, destination = "", travelSpeed = 90, name= "") -> None:
        name = namesList.pop()
        destination = locations[random.randint(0,len(locations)-1)]
        super().__init__(destination, travelSpeed, name)      

class cat3(Storms):
    def __init__(self, destination = "", travelSpeed = 80, name=  "") -> None:
        name = namesList.pop()
        destination = locations[random.randint(0,len(locations)-1)]
        super().__init__(destination, travelSpeed, name) 

class cat2(Storms):
    def __init__(self, destination = "", travelSpeed = 70, name= "") -> None:
        name = namesList.pop()
        destination = locations[random.randint(0,len(locations)-1)]
        super().__init__(destination, travelSpeed, name)

class cat1(Storms):
    def __init__(self, destination = "", travelSpeed = 60, name= "") -> None:
        name = namesList.pop()
        destination = locations[random.randint(0,len(locations)-1)]
        super().__init__(destination, travelSpeed, name)

class tStorm(Storms):
    def __init__(self, destination = "", travelSpeed = 50, name= "") -> None:
        name = namesList.pop()
        destination = locations[random.randint(0,len(locations)-1)]
        super().__init__(destination, travelSpeed, name)

class tDepress(Storms):
    def __init__(self, destination = "", travelSpeed = 40, name= "") -> None:
        name = str(count)
        destination = locations[random.randint(0,len(locations)-1)]
        super().__init__(destination, travelSpeed, name)


def stormSim():
    count = 1
    for x in range(25):
        chance = random.randint(0,100)
        if chance < 1:
            hurricane = cat5()
            hurricane.info()
        elif chance < 4:
            hurricane = cat4()
            hurricane.info()
        elif chance < 10:
            hurricane = cat3()
            hurricane.info()
        elif chance < 20:
            hurricane = cat2()
            hurricane.info()
        elif chance < 32:
            hurricane = cat1()
            hurricane.info()
        elif chance < 50:
            hurricane = tStorm()
            hurricane.info()
        elif chance < 70:
            hurricane = tDepress()
            hurricane.info()
        elif  chance < 100:
            print("Skies are clear! ")
            print("")
        count += 1

stormSim()