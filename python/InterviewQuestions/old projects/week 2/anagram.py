def sortList(word1):
    word1 = word1.lower()   # makes all characters in string lowercase
    word1 = list(word1)     # turns string into a list
    for x in range(0,len(word1)-1):     # sorts list 
        for y in range(x,len(word1)):
            if word1[y] < word1[x]:
                temp = word1[y]
                word1[y] = word1[x]
                word1[x] = temp
    print(word1)
#---------------------------------------------------------------
def isAnagram(word1,word2):
    word1 = sortList(word1)
    word2 = sortList(word2)

    if word1 == word2:
        return True
    else:
        return False
#---------------------------------------------------------------   
word1 = input("First word. ")
word2 = input("Second word. ")
print(isAnagram(word1,word2))




