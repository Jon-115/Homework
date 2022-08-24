def leetspeak(word):
    letters = {}

    newWord = ""
    
    for x in word:
        if x in letters.keys():
            newWord  = newWord + letters.