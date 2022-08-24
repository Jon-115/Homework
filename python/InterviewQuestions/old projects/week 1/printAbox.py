width = int(input("Width? "))
height = int(input("Height? "))
count = 1
dot = ""

for index in range(1,height+1):
    if count == 1 or count == height:
        for index in range(1,width+1):
            dot = dot + "*"
    elif count != height - 1 or count != 1:
        for index in range(1,width+1):
            if index == 1:
                dot = dot + "*"
            elif index != width:
                dot = dot + " "
            elif index == width:
                dot = dot + "*"
    print(dot)
    dot = ""
    count = count + 1


        