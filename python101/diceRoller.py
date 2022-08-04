import random
print("Let's roll a dice! ")
sides = input("How many sides should it have? (2-20): ")
sides = int(sides)
print(random.randint(1,sides))