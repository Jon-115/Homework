numList = [67,34,54,12,60,38,11,45]

def sortInt (myList: list)->list:
    temp = 0
    j = 0
    max = len(myList)
    while j < max - 1:
        i = j + 1
        while i < max:
            if myList[j] > myList[i]:
                #print(j," ",i)
                temp = myList[i]
                myList[i] = myList[j]
                myList[j] = temp
            i += 1
        j += 1

    
    return myList
    
print(sortInt(numList))

