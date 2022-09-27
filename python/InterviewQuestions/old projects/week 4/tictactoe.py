import random
# import unittest

# def tictactoe():
board = [[' ', ' ', ' '],
         [' ', ' ', ' '],
         [' ', ' ', ' ']]
xAxis = 0
yAxis = 0
gameover = False


def tileSpot(sym, player):
    xAxis = random.randint(0,2)
    yAxis = random.randint(0,2)

    while board[xAxis][yAxis] != ' ':
        xAxis = random.randint(0,2)
        yAxis = random.randint(0,2)

    board[xAxis][yAxis] = sym
    print('%s placed an %s on (%s, %s)' % (player, sym, xAxis, yAxis))
    
    
def checkWin(sym,player):
    # board[xAxis][yAxis]
    if sym == board[0][0] and sym == board[0][1] and sym == board[0][2]: # first column of board
        print(player + ' wins by filling first column')
        return True
    elif sym == board[1][0] and sym == board[1][1] and sym == board[1][2]: # second column of board
        print(player + ' wins by filling second column')
        return True
    elif sym == board[2][0] and sym == board[2][1] and sym == board[2][2]: # third column of board
        print(player + ' wins by filling third column')
        return True
    elif sym == board[0][0] and sym == board[1][0] and sym == board[2][0]: # first row of board
        print(player + ' wins by filling first row')
        return True
    elif sym == board[0][1] and sym == board[1][1] and sym == board[2][1]: # second row of board
        print(player + ' wins by filling second row')
        return True
    elif sym == board[0][2] and sym == board[1][2] and sym == board[2][2]: # third row of board
        print(player + ' wins by filling third row')
        return True
    elif sym == board[0][0] and sym == board[1][1] and sym == board[2][2]: # backslash of board
        print(player + ' wins by filling a backslash')
        return True
    elif sym == board[2][0] and sym == board[1][1] and sym == board[0][2]: # forward slash of board
        print(player + ' wins by filling a forward slash')
        return True
    else:
        return False

count = 0
while gameover == False:
    if count % 2 == 0:
        player = 'Player 1'
        symbol = 'X'
    else:
        player = 'Player 2'
        symbol = 'O'

    if count == 9:
        print('It was a tie.')
        break

    tileSpot(symbol,player)

    print('\n %s | %s | %s ' % (board[0][0], board[1][0], board[2][0] ))
    print('-----------')
    print(' %s | %s | %s ' % (board[0][1], board[1][1], board[2][1] ))
    print('-----------')
    print(' %s | %s | %s ' % (board[0][2], board[1][2], board[2][2] ))
    print('\n')

    gameover = checkWin(symbol,player)

    count += 1


# class TestGame(unittest.TestCase):

#     def tictactoe(self):
#         self.assertEquals(tictactoe(),)