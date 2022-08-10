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
        if chanceOf(1, 3) == True:
            self.woodchuck += 1 
            print('A woodchuck has moved into your neighborhood! You have %s woodchunks'% self.woodchuck)
            
    def moreRain(self):         # Random chance of it raining
        if chanceOf(1, 30) == True:
            isRaining = True
            self.waterGain()
            print('Its a miracle! It has started to rain!')
    
#-----------------------------------------------------------------------------------
def runGame(DcGarden):          # calls for the functions for every turn
    DcGarden.isRaining = False
    print('Turn: #%d ' % turn)
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
    #print("")
    print("Water level:",DcGarden.waterlevel)
    print('We have ' + str(int(DcGarden.tree)) + ' trees.')

def treeorGnome(turn):          # Gives either gnome or tree every 10 turns
    if turn % 10 == 0:
        randNum = random.randint(0,9)
        if randNum >= 5:
            print("The Goddess of the Forest has blessed you with a tree! ")
            DcGarden.tree += 1
        elif randNum < 5:
            print("The God of Storms has bestowed you a gnome! ")
            DcGarden.gnome += 1
    



# Run the game
#-----------------------------------------------------------
# treeNum = useful.intput("Enter the amount of trees. ")
# gnomeNum = useful.intput("Enter the amount of gnomes. ")
# woodchuckNum = useful.intput("Enter the amount of woodchucks.\n ")
# DcGarden = Garden(treeNum,gnomeNum,woodchuckNum)

DcGarden = Garden(4,3,0)

turn = 1
while DcGarden.tree < 11:
    runGame(DcGarden)
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

