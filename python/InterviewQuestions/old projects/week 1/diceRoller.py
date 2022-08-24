import random
sides = ""
print("Let's roll a dice! ")
while str.isdigit(sides) == False:
    sides = input("How many sides should it have? (2-20): ")
    try:
        sides = int(sides)
        if sides < 2 or sides > 20:
            sides = str(sides)
            sides = ""
    except:
        print
    sides = str(sides)
sides = int(sides)
num = random.randint(1,sides)
print("You rolled a " + str(num))