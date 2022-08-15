### Delta has not paid their pilots and are now experiencing delays nationwide.
# Due to this, they now need an algorithm to kick people off of planes while
# maintaining a passing happiness score. If a passing happiness score is not possible,
# maximize the happiness score the best you can.

# first class - 80% chance of leaving a negative review on Google
            # - 50% chance of refusing to move
            # - 1% chance of punching the flight attendant in the face

# business class - 70% chance of leaving a negative review on Google
               # - 30% chance of refusing to move
               # - 2% chance of punching the flight attendant in the face

# comfort+ - 50% chance of leaving a negative review on Google
         # - 20% chance of refusing to move
         # - 5% chance of punching the flight attendant in the face

# economy - 10% chance of leaving a negative review on Google
        # - 10% chance of refusing to move
        # - 15% chance of punching the flight attendant in the face
        # - special ability - if passenger decides to Chuck Norris the
        # flight attendant, 5% chance the attendant is KO'd resulting
        # in the entire flight being canceled

# * Each negative Google review is -1 on the happiness meter.
# * Each passenger that refuses to move, delays the flight by 5 minutes.
# Happiness -3 for every 30 minutes the flight is delayed.
# * Happiness -10 for a flight attendant getting punched in the face,
# and -100 if the flight is cancelled.

# * On a plane, there are 16 rows and 4 seats which are denoted by numbers,
# and the seat by letters 'A', 'B', 'C', etc.
# * First class is in rows 1-2, business 3-5, comfort+ 6-10, economy 11-16.
# * Happiness starts at 100. Passing happiness meter is 70.

# * Each flight needs to remove 6 people.

import random

# Define the 6 classes: Plane, Passenger, FirstClass, BusinessClass, ComfortPlus, Economy
#----------------------------------------------------------------------------------------
class Plane:
        def __init__(self):
                self.happiness = 100
                self.overbooked = 6
                self.delayMeter = 0
                self.round = 1
                self.manifest = self.createPlane()

        def createPlane(self):
                self.seatDict = {}
                self.rows = range(1, 17)
                self.seats = ['A', 'B', 'C', 'D']
                for row in self.rows:
                        strRow = str(row)
                        for seat in self.seats:
                                seatNum = strRow + seat
                                if row < 3:
                                        self.seatDict[seatNum] = 'First Class'
                                elif row < 6:
                                        self.seatDict[seatNum] = 'Business Class'
                                elif row < 11:
                                        self.seatDict[seatNum] = 'Comfort+'
                                else:
                                        self.seatDict[seatNum] = 'Economy'
                return self.seatDict
                # print(self.seatDict)

        def negReview(self): # function called if a negative review was left
                self.happiness -= 1
                self.overbooked -= 1
                print('The passenger left a bad Google Review after being asked to move, but moved anyway.')
            
        def refusedMove(self): # function called if passenger refused to move
                self.delayMeter += 5
                print("\033[33mThe passenger refused to move and delayed takeoff.\033[0m")

        def delayFlight(self): # function called if delay meter reaches increments of 30 minutes
                self.happiness -= 3
                print("\033[33mThe flight was delayed by long enough to make the passengers unhappy.\033[0m")
        def punchedFace(self): # function called if passenger threw hands
                self.happiness -= 10
                self.overbooked -= 1
                print("\033[31mThe passenger punched a flight attendant right in the kisser! He gone!\033[0m")

        def chuckNorris(self):
                self.happiness -= 100
                print("\033[31mThe passenger went full Chuck Norris on the flight attendant!\033[0m")

        def cancelledFlight(self):
                self.happiness -= 100
                print("\033[31mThe flight was cancelled!\033[0m")

        def getStats(self):
                print('\n-------------------------')
                print('Round: %d' % self.round)
                print(f"Current Delay:  % {self.delayMeter}")

                if(self.happiness > 90):
                        print(f"\033[32mHappiness Level: % {self.happiness}\033[0m")
                elif(self.happiness >= 80 and self.happiness < 90):
                        print(f"\033[33mHappiness Level: % {self.happiness}\033[0m")
                elif(self.happiness < 80):
                        print(f"\033[31mHappiness Level: % {self.happiness}\033[0m")
                print('Overbooked Passengers Remaining: %d' % self.overbooked)
        
        def endTurn(self):
                self.round += 1


class Passenger:
        def __init__(self, review: int, move: int, punch: int) -> None:
                self.review = review
                self.move = move
                self.punch = punch


class FirstClass(Passenger):
        def __init__(self, review = 80, move = 50, punch = 1) -> None:
                super().__init__(review, move, punch)


class BusinessClass(Passenger):
        def __init__(self, review = 70, move = 30, punch = 2):
                super().__init__(review, move, punch)


class ComfortPlus(Passenger):
        def __init__(self, review = 50, move = 20, punch = 5):
                super().__init__(review, move, punch)


class Economy(Passenger):
        def __init__(self, review = 10, move = 10, punch = 15, chuck = 5):
                super().__init__(review, move, punch)
                self.chuck = chuck
#--------------------------------------------------------------------------------

### Stylize the terminal output ###
# print("\033[31mThis is red font.\033[0m")
# print("\033[32mThis is green font.\033[0m")
# print("\033[33mThis is yellow font.\033[0m")
# print("\033[34mThis is blue font.\033[0m")
# print("\033[38mThis is the default font. \033[0m")

# Run the simulator
#--------------------------------------------------------------------------------
plane = Plane()

while plane.happiness > 70 and plane.overbooked > 0:
        plane.getStats()
        
        while True:
                # Let the user pick one of the four seat classes
                userInput = input('Select a class. \n"f" for first class. \n"b" for business class. \n"c" for comfort+. \n"e" for economy. ')
                if userInput == 'f':
                        passenger = FirstClass()
                        break
                elif userInput == 'b':
                        passenger = BusinessClass()
                        break
                elif userInput == 'c':
                        passenger = ComfortPlus()
                        break
                elif userInput == 'e':
                        passenger = Economy()
                        break
                else:
                        print("Not a class, try again.")
                        
        # Main conditional logic
        if random.random() * 100 < passenger.punch:
                plane.punchedFace()
                if userInput == 'e':
                        chance = random.random() * 100
                        if chance < passenger.chuck:
                                        plane.chuckNorris()
        elif random.random()*100 < passenger.move:
                plane.refusedMove()
        elif random.random()*100 < passenger.review:
                plane.negReview()
        else:
                plane.overbooked -= 1
                print("\033[32mThe passenger left without a hitch.\033[0m")

        # Display warning that flight was delayed long enough to make passengers unhappy
        if plane.delayMeter % 30 == 0 and plane.delayMeter != 0:
                plane.delayFlight()
        
        # End the turn
        plane.endTurn()

# End game
if plane.overbooked > 0:
        print("\033[34mSorry! Better luck next time.\033[0m")
else:
        print("\033[32mYou have successfully gotten all 6 overbooked passengers off the plane!\033[0m")
