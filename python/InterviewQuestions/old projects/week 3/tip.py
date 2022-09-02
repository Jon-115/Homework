billAmount = input('Total bill amount? ')
billAmount = float(billAmount)

while True:
    service = input('Level of service? ')
    if service == 'good':
        tip = .2 * billAmount 
        break
    elif service == 'fair':
        tip = .15 * billAmount
        break
    elif service == 'bad':
        tip = .1 * billAmount
        break
    else:
        print('Not a service option')
        continue


print('Tip amount: $%.2f' % tip)
print('Total amount: $%.2f' % (tip+billAmount))

while True:
    ans = input('Would you like to split the check? y for yes, n for no. ')
    if ans == 'y':
        ans = input('Between how many people? ')
        ans = float(ans)
        print('The total amount for each person is $%.2f' %((tip+billAmount)/ans))
        break
    elif ans == 'n':
        print('Total amount: $%.2f' % (tip+billAmount))
        break
    else:
        print('Incorrect input. Try again. ')
        continue


