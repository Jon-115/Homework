import unittest

def decode(num):
    print(num)
    letter = ''
    numList = {'1':'','2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
    
    if num[0] == '0' or num[0] == '#' or num[0] == '*':
        sym = num[0]
        if sym == '0':
            sym = ' '

        for x in range(len(num)):
            letter += sym
        return letter
    elif num[0] == '1':
        return letter

    temp = numList[num[0]]
    print(num[0])
    letter = temp[len(num)-1]

    return letter
#-----------------------------------------------------------------------------------------------------------
def interpret(code: list): 

    if str.isdigit(code) == False:
        return ':('

    temp = code[0]
    word = ''

    for i in range(len(code)-1):
        
        if temp != code[i+1]:
            word += decode(temp)
            temp = code[i+1]
        else:
            temp += temp

    word += decode(temp)
    return word
            
print(interpret('44335551555666'))
#-----------------------------------------------------------------------------------------------------------
# class TestDecode(unittest.TestCase):

#     def testdecode(self):
#         self.assertAlmostEquals(interpret(''),'')

# unittest.main()