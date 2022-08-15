num = ""
while str.isdigit(num) == False:
    num = input("Enter a number: ")
    if num[0] == "-":
        num = num[1:]
num = int(num)
if num%2 == 0:
    print("even")
else:
    print("odd")
