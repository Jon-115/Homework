import unittest

dogList = [{"breed":"G","weight":88,"fur":("black","red")},{"breed":"G","weight":30,"fur":("black","white")},{"breed":"G","weight":40,"fur":("black","brown")},
{"breed":"G","weight":60,"fur":("black","brown")},{"breed":"G","weight":2,"fur":("black","brown")},{"breed":"G","weight":49,"fur":("blue","red")},]

answer = [{'breed': 'G', 'weight': 88, 'fur': ('black', 'red')}, {'breed': 'G', 'weight': 40, 'fur': ('black', 'brown')}, 
{'breed': 'G', 'weight': 60, 'fur': ('black', 'brown')},{"breed":"G","weight":2,"fur":("black","brown")},]

def sortDogs(myList:list)->list:
    newList = []
    for x in myList:
        if x["weight"] > 50:
            newList.append(x)
        elif x["fur"][0] == "brown" or x["fur"][1] == "brown":
            newList.append(x)
    
    return newList

sortdogList = sortDogs(dogList)
print(sortdogList)

class Testdogs(unittest.TestCase):
    def testdogs(self):
        self.assertEqual(sortDogs(dogList),answer)

unittest.main()