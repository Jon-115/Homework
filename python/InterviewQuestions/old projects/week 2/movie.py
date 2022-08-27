likeList = ["\U0001F44D", "\N{thumbs up sign}",  "\N{Face with Open Mouth Vomiting}", "\U0001F44D", "\U0001f929", "\N{thumbs down sign}", 
"\U0001F44E", "\U0001F92E", "\U0001f929", "\N{thumbs down sign}", "\N{thumbs up sign}", "\U0001F44D", "\U0001F44D", "\N{Face with Open Mouth Vomiting}",
 "\N{thumbs down sign}", "\U0001F44D", "\U0001f929", "\U0001F44D", "\N{thumbs down sign}", "\N{thumbs down sign}"]

def likeMovie(myList: list):
    counter = 0
    ratio = 0

    for x in likeList:

        if x == '\U0001F44D' or x == '\N{thumbs up sign}' :
            counter += 1
            ratio += 1
        elif x == '\U0001f929':
            counter += 2
            ratio += 1
        elif x == '\N{thumbs down sign}' or x == '\U0001F44E' :
            counter += -1
        elif x == '\N{Face with Open Mouth Vomiting}' or x == '\U0001F92E':
            counter += -2
    
    per = int(ratio / len(myList) * 100)
    print(f"The rating of the movie was {counter}, with {per}%" + " of people enjoying the movie")
    return (counter,per)

print(likeList)
likeMovie(likeList)
