import unittest

tl1 = [1,1,2,None]
al1 = [1,1,2,2]

tl2 = [1,None,None]
al2 = [1,1,1]

tl3 = [2,None,1,None]
al3 = [2,2,1,1]

tl4 = [None,2,None]
al4 = [None,2,2]

tl5 = [None,None,1]
al5 = [None,None,1]

def newNone(myList):

    for x in range(1,len(myList)):
        if myList[x] == None:
            myList[x] = myList[x-1]

    return myList



class TestNewnone(unittest.TestCase):

    def testNewnone(self):
       self.assertAlmostEquals(newNone(tl5),al5)

unittest.main()