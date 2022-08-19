


file = open("/Users/jonathanbatalla/DigitalCrafts/web-ft-08-22/Code/python/week3/sample/theWasteLand.txt", "r")  
#/Users/jonathanbatalla/DigitalCrafts/web-ft-08-22/Code/python/week3/sample/theRoadNotTaken.txt
#/Users/jonathanbatalla/DigitalCrafts/web-ft-08-22/Code/python/week3/sample/theWasteLand.txt
#/Users/jonathanbatalla/DigitalCrafts/web-ft-08-22/Code/python/week3/sample/thisIsJustToSay.txt

def mostLetter(file):
    
    mostWord = {}                                                  
    for line in file:
        line = line.lower()
        line = line.replace(" ","")
        for letter in line:
            if letter != "\n":
                if letter in mostWord.keys():
                    mostWord[letter] = mostWord[letter] + 1
                else:
                    mostWord[letter] = 1
    print(mostWord)
    
    lowest = 0
    winner = ""
    for num in mostWord:
        if mostWord[num] > lowest:
            lowest = mostWord[num]
            winner = num
    print("The letter %s has the most words at " % winner,lowest)
#------------------------------------------------------------------------------------------------------------------------------------

def mostWord(file):

    wordCount = {}
    for line in file:
            strSplit = line.split()
            for word in strSplit:
                word = word.lower()
                if word in wordCount.keys():
                    wordCount[word] += 1
                else:
                    wordCount[word] = 1
    count = 0
    highest = ""
    for word in wordCount:
        if wordCount[word] > count:
            count = wordCount[word]
            highest = word
    print("most occurrences: ", highest)
    print("count: ", count)
    print(wordCount)
    file.close()

mostLetter(file)
mostWord(file)

file.close() 


        
