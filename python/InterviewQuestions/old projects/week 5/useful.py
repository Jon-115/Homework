# outputs intgers only
def intput(phrase: str) -> str:
    num = input(phrase)                                       #gets input/num
    if str.isdigit(num) == True and len(num) == 4:            #checks if num is a num
        return num
    while str.isdigit(num) == False or len(num) != 4 :
        if str.isdigit(num)== True and len(num) == 4:        
            return num
        else:                                                 #cycle again
            num = input("Try again. ")
            continue
    return num
           


    