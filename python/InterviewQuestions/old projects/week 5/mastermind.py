import random
import useful
import unittest
    
def checkWin(guess,num):

    clue = ''
    p1 = num[0]
    p2 = num[1]
    p3 = num[2]
    p4 = num[3]
    ans = (p1 * 1000) + (p2 * 100) + (p3 * 10) + p4

    g1 = int(guess[0])
    g2 = int(guess[1])
    g3 = int(guess[2])
    g4 = int(guess[3])
    guess = int(guess)
    
    if guess == ans:
        clue = 'RRRR'
        print('You Won')
        return clue
    else:
        if g1 == p1:
            clue += 'R'
        elif g1 in num:
            clue += 'Y'
        else:
            clue += 'B'

        if g2 == p2:
            clue += 'R'
        elif g2 in num:
            clue += 'Y'
        else:
            clue += 'B'

        if g3 == p3:
            clue += 'R'
        elif g3 in num:
            clue += 'Y'
        else:
            clue += 'B'

        if g4 == p4:
            clue += 'R'
        elif g4 in num:
            clue += 'Y'
        else:
            clue += 'B'

    return clue

def startGame():

    p1 = random.randint(0,9)
    p2 = random.randint(0,9)
    p3 = random.randint(0,9)
    p4 = random.randint(0,9)
    num = [p1,p2,p3,p4]
    print(num)
    count = 0
    clue = ''

    while clue != 'RRRR' and count < 10:
        
        guess = useful.intput('guess a number. ')
        clue = checkWin(guess,num)
        print(clue)
        count += 1
    
    if count == 10:
        print('You Lost')

# startGame()


class TestGame(unittest.TestCase):

    def testCheckWin(self):
        self.assertAlmostEqual(checkWin('1234',[1,2,3,4]),'RRRR')

unittest.main()