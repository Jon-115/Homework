def sortList(num):

    for y in range(len(num)):
        for x in range(len(num)-1-y):
            if num[x] > num[x+1]:
                temp = num[x+1]
                num[x+1] = num[x]
                num[x] = temp
    print(num)

numList = [12,1,34,2,35,11,56,8,7,24,5]

sortList(numList) 