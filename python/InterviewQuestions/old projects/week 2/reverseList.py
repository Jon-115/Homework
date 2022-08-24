
# def less5000(List: list) -> list:
#     newList = []
    
#     for index in List:
#         if int(index["id"]) < 500000:
#             newList.append(index)

#     return newList

List = [1,2,3,4,5,6,7,8,9,10,]

def reverseList(myList: list)-> list:
    newList = []
    for index in range(len(myList)):
        count = -index - 1
        newList.append(myList[len(myList)+count])
    return newList

print(reverseList(List))


