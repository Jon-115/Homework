studentName = ["jon","sod","tod","smith","derk",'tod',"jon"]

def makeDict(list1:list) -> dict:   
    dict1 = {}
    for name in list1:
        if name in dict1.keys():
            dict1[name] = dict1.get(name) + 1
        else:
            dict1[name] = 1
    return dict1

def dupeNames(dict1:dict):
    newList = []
    for name in dict1:
        if dict1.get(name) > 1:
            newList.append(name)
    return newList

mydict = makeDict(studentName)
print(mydict)
dupeList = dupeNames(mydict)
print(dupeList)