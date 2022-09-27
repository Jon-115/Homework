import unittest

names = ['Jonathan','Khan','Dre','Matt','Fiona','Jorge','Jordan','Carlos','Wes','An','Dez']
answer = ['Wes','Matt','Khan','Jorge','Jordan','Jonathan','Fiona','Dre','Dez','Carlos','An']

def sortList(myList):

    for x in range(len(myList)):
        for y in range(len(myList)-1-x):
            if myList[y] < myList[y+1]:
                myList[y], myList[y+1] = myList[y+1], myList[y]
    return(myList)

print(sortList(names))

class TestSort(unittest.TestCase):

    def testsortlist(self):
        self.assertEqual(sortList(names),answer)


unittest.main()