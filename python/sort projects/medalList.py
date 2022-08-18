scores = {'kate':12,'todd':14,'matt':5,'mark':8,'pat':19}

def sortDict(Dict1):
    for x in Dict1:
        if Dict1[x] > Dict1[x+1]:
            temp = x
            Dict1[x] = Dict1[x+1]
            Dict1[x+1]= x


sortDict(scores)