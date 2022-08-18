id = ""
while str.isdigit(id) == False:
    id = input("What is your id? ")
id = int(id)
if id <= 100:
    print("1st ")
elif id < 250:
    print("2nd ")
else:
    print("all reservations taken. ")

