repeat = '.|.'
#-----------------------------------------------
def createLine(count,length):
    amount = int((length-(3*count))/2)
    line = []

    for x in range(count):
        line.append(repeat)

    for x in range(amount):
        line.append('-')

    for x in range(amount):
        line.insert(0,'-')

    print(''.join(line))
    return line
#-----------------------------------------------
def createWelcome(length):
    welcome ='WELCOME'
    amount = int((length-7)/2)
    line = []

    line.append(welcome)

    for x in range(amount):
        line.append('-')

    for x in range(amount):
        line.insert(0,'-')

    print(''.join(line))
    return line
#-----------------------------------------------
def createMat(height,length):
    count = 1

    while count < height:
        createLine(count,length)
        count+= 2

    createWelcome(length)

    count = (height - 2)

    while count > 0:
        createLine(count,length)
        count-= 2
#-----------------------------------------------
createMat(15,45)
