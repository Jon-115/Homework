# outputs intgers only
def intput(phrase: str) -> int:
    num = input(phrase)                     #gets input/num
    if str.isdigit(num) == True:            #checks if num is a num
        return int(num)
    while str.isdigit(num) == False:
        if str.isdigit(num[1:]) == True:    #checks if num is neg.
            return int(num) 
        else:                               #cycle again
            num = input("Try again. ")
            continue
    return int(num)
           


    