import random
import useful
#-----------------------------------------------------------------------------------------------
def chanceOf(numOf, chance):    # calculates chances of something happening and return True or False
    randomNum = random.random() * 100
    randomNum = int(randomNum)
    if numOf * chance >= randomNum:
        return True
    else:
        return False

def input123(Phrase):           # Only accepts input 1,2,3,or 4
    i = 0
    while i < 100:
        x = input(Phrase)
        if x == "1":
            return "1"
        elif x == "2":
            return "2"   
        elif x == "3":
            return "3"  
        elif x == "4":
            return "4"  
        else:
            continue
    i += 1

#Create the environment
#------------------------------------------------------------------------------------------------

class Garden:
    def __init__(self, tree: int, gnome: int, woodchuck: int):
        self.tree = tree
        self.gnome = gnome
        self.woodchuck = woodchuck
        self.isRaining = False
        self.waterlevel = 0
        self.waterloss = 10


    def waterLoss(self):        # Determines how much water is lost and if it can't lose any it sets water level to 0
        self.waterloss = 10
        if self.waterlevel - (self.waterloss - (self.tree * 2)) <= 0:
            self.waterlevel = 0
        else:
            self.waterloss = self.waterloss - (self.tree * 2)
            if self.waterloss > 0:
                self.waterlevel = self.waterlevel - self.waterloss
                print("Water level has decreased by %s! " % self.waterloss)

    def waterGain(self):        # Increases water level by 40
        self.waterlevel = self.waterlevel + 20

    def rainChance(self):       # Determines what the chances are of it Raining
        numGnome = self.gnome
        if chanceOf(numGnome, 5) == True:
            self.isRaining = True
            print("It is Raining! ")
        else:
            print("Guess there's no rain today. ")

    def treeLoss(self):         # Determines what the chances are of lossing a tree
        numWoodchuck = self.woodchuck
        if chanceOf(numWoodchuck, 5) == True:
            print('A woodchuck destroyed a tree!')
            self.tree = self.tree - 1

    def treeGain(self):         # Increases trees by 1 if water level is at or more than 100
        if self.waterlevel >= 100:
            self.tree = self.tree + 1
            print("A tree has risen from the ground. ")
            self.waterlevel = 0

    def woodchuckGuest(self):   # Random chances of an increase in woodchucks by 1
        if chanceOf(1, 7) == True:
            self.woodchuck += 1 
            print('A woodchuck has moved into your neighborhood! You have %s woodchucks'% self.woodchuck)
            
    def moreRain(self):         # Random chance of it raining
        if chanceOf(1, 30) == True:
            isRaining = True
            self.waterGain()
            print('Its a miracle! It has started to rain!')
    
    def endWeek(self,turn):                 # user can sacrifice a gnome or tree to reduces the number of woodchucks by 1
        print("You have %s trees, %s gnomes, %s woodchucks. " %(self.tree, self.gnome, self.woodchuck))
        if turn % 7 == 0:
            answer = input123('''\nEnd of week %s. Would you like to sacrifice a tree or 2 gnomes to rid a woodchuck?
                            \nPress 1 to sacrifice a tree. \nPress 2 to sacrifice 2 gnomes. \nPress 3 to sacrifice a tree and a  2 gnome. \nPress 4 to continue \n'''% int((turn/7)))
            if answer == "1":
                self.tree -= 1
                self.woodchuck -= 1
            elif answer == "2":
                self.gnome -= 2
                self.woodchuck -= 1
            elif answer == "3":
                self.gnome -= 2
                self.tree -= -1
                self.woodchuck -= 1
            elif answer == "4":
                print

    def war(self):   
        if self.gnome >= 2 and self.woodchuck >= 2:       # Chance for gnomes and woodchucks to fight each other. 
            if chanceOf(1, 2) is True:                    # Could result in the loss of either 1 gnome or 1 woodchuck
                print("The God of War, Ares, has incited violence in the gnomes and woodchucks! ")             
                if chanceOf(1,49) == True:
                    print("War broke out and woodchucks won.")
                    self.gnome -= 1
                else:
                    print("War broke out and gnomes won.")
                    self.woodchuck -= 1
            else:
                print('There is peace between gnomes and woodchucks.')


    def underworld(self): # Chance to summon a hellhound to wipeout the woodchucks 
        if self.woodchuck > 2:
            if chanceOf(1, 2) == True:
                print('The underworld god, Hades, summoned a hellhound, killing all of the woodchucks.')
                self.woodchuck = 0
            
#-----------------------------------------------------------------------------------
def treeorGnome(turn):          # Gives either gnome or tree every 10 turns
    if turn % 10 == 0:
        randNum = random.randint(0,9)
        if randNum >= 5:
            print("The Goddess of the Forest has blessed you with a tree! ")
            DcGarden.tree += 1
        elif randNum < 5:
            print("The God of Storms has bestowed you a gnome! ")
            DcGarden.gnome += 1
    

def runGame(DcGarden,turn):          # calls for the functions for every turn
    DcGarden.isRaining = False
    print('''\n-----------------------------
    Day: #%d
    \b\b\b\b\b-----------------------------''' % turn)
    DcGarden.rainChance()
    if DcGarden.isRaining == True:
        DcGarden.waterGain()
        print("The water level has risen. ")
    else:
        DcGarden.waterLoss()
    DcGarden.treeGain()
    DcGarden.treeLoss()
    DcGarden.woodchuckGuest()
    DcGarden.moreRain()
    DcGarden.endWeek(turn)
    DcGarden.underworld()
    DcGarden.war()
    #print("")
    print("Water level:",DcGarden.waterlevel)
    print('We have ' + str(int(DcGarden.tree)) + ' trees.')

# Run the game
#-----------------------------------------------------------
# treeNum = useful.intput("Enter the amount of trees. ")
# gnomeNum = useful.intput("Enter the amount of gnomes. ")
# woodchuckNum = useful.intput("Enter the amount of woodchucks.\n ")
# DcGarden = Garden(treeNum,gnomeNum,woodchuckNum)

easy = Garden(5,4,1)                            # Setting difficulties
medium = Garden(4,4,1)
hard = Garden(3,3,2)
impossible = Garden(3,3,3)

difficulty = input123('''Choose your difficulty. Press 1 for "Easy". Press 2 for "Medium". Press 3 for "Hard". Press 4 for "Impossible". ''')

if difficulty == "1":
    DcGarden = easy                             # Setting difficulties
elif difficulty == "2":
    DcGarden = medium
elif difficulty == "3":
    DcGarden = hard
elif difficulty == "4":
    DcGarden = impossible

turn = 1
while DcGarden.tree < 11:
    runGame(DcGarden, turn)
    treeorGnome(turn)
    if DcGarden.tree >= 10:
        print("The Gods rejoice your victory! ")
        break
    elif DcGarden.tree == 0:  
        print("The Gods laugh at your defeat! ")
        break
    
    print("")
    #input("")
    turn += 1

