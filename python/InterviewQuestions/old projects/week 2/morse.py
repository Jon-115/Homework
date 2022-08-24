
wordList = ["gin","zen","gig","msg"]

def morse(myList:list)-> int:
    morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
    newList = []
    
    for index in myList:
        newWord = ""
        for letter in index:
            i = ord(letter) - 97
            #print(i)
            #print(morse[i])
            newWord = newWord + morse[i]
        if newWord not in newList:
            newList.append(newWord)

    print("There are %i different transformations: " % len(newList), newList)
    return len(newList)

print(morse(wordList))