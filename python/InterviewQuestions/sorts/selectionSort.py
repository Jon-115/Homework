def sortList(num1):
    for x in range(0,len(num1)-1):         # Creates first Pointer
        for y in range(x,len(num1)):       # Creates second Pointer
            if num1[y] < num1[x]:          # Compares the value of the Pointer at that instance
                temp = num1[y]             # Swaps the numbers in the List
                num1[y] = num1[x]
                num1[x] = temp
    print(num1)

numList = [12,1,34,2,35,11,56,8,7,24,5]

sortList(numList) 