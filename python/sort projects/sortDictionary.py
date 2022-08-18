student = {
    "id": 790283,
    "name": "Dre Taylor",
    "class": "Senior",
    "GPA": 3.87
}

#print(student["GPA"])


student1 = {
    "id": "478923",
    "name": "Wes Fountain",
    "bootcamp": "Digitalcrafts"
}


student2 = {
    "id": "578490",
    "name": "Jorge Rodriguez",
    "bootcamp": "Digitalcrafts"
}

student3 = {
    "id": "453789",
    "name": "Khanh Trinh",
    "bootcamp": "Digitalcrafts"
}

student4 = {
    "id": "945890",
    "name": "Jonathan",
    "bootcamp": "Digitalcrafts"
}

student5 = {
    "id": "578909",
    "name": "Fiona Eckert",
    "bootcamp": "Digitalcrafts"
}

digitalcrafts_class = [student1, student2, student3, student4, student5,student]

def sortList(newList: list)-> list:
    temp = {}
    for x in range(0,len(newList)-1):                           #first loop
        for y in range(x,len(newList)):                       #second loop
            if int(newList[x]["id"]) > int(newList[y]["id"]):   #check for the switch
                #print(x," ",y)
                temp = newList[y]["id"]
                newList[y]["id"] = newList[x]["id"]
                newList[x]["id"] = temp
    return newList
#print(digitalcrafts_class)
print(sortList(digitalcrafts_class))

# def myFunc(e):
#     return e["id"]
# digitalcrafts_class.sort(key=myFunc)
# print(digitalcrafts_class)





