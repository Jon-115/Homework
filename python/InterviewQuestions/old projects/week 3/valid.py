student1 = {
    'name':'bob',
    'email':'bob@gmail.com',
    'phone':'(213)-123-3213',
    'zip':'92345'
}

student2 = {
    'name':'hank',
    'email':'hank@hotmail.com',
    'phone':'(564)-342-8902',
    'zip':'23456'
}

student3 = {
    'name':'tom',
    'email':'tom@yahoo.com',
    'phone':'(765)-563-2391',
    'zip':'63423'
}


people = [student1, student2, student3]
#-------------------------------------------------------------------------------------------------------------------------------------------------
def vEmail(email: str) -> bool:
    valid = False

    if '@' not in email:
        return valid

    temp = email.find('@')
    if email[temp:len(email)] == '@gmail.com' or email[temp:len(email)] == '@hotmail.com' or email[temp:len(email)] == '@yahoo.com':
        valid = True
    return valid
#-------------------------------------------------------------------------------------------------------------------------------------------------
def vPhone(phoneNum: str) -> bool:
    valid = False

    if len(phoneNum) != 14:
        return valid

    for x in range(len(phoneNum)):
        if phoneNum[x].isdigit() == True:
            phoneNum = phoneNum.replace(phoneNum[x],'x')
    
    if phoneNum == '(xxx)-xxx-xxxx':
        valid = True
    
    #print(phoneNum)
    return valid
#-------------------------------------------------------------------------------------------------------------------------------------------------
def vZip(zip:str) -> bool:
    valid = False

    if len(zip) != 5:
        return valid

    if int(zip) in range(501,99951):
        valid = True
   
    return valid
#-------------------------------------------------------------------------------------------------------------------------------------------------
def vInfo(person: dict) -> bool:
    valid = False
    
    if vEmail(person['email']) != True:
        print('email was not valid.')
        return valid
    if vPhone(person['phone']) != True:
        print('Phone number was not valid.')
        return valid
    if vZip(person['zip']) != True:
        print('Zip code was not valid.')
        return valid

    valid = True
    return valid
#-------------------------------------------------------------------------------------------------------------------------------------------------
def vList(myList: list) -> bool:
    valid = False

    for x in myList:
        if vInfo(x) == False:
            print(x['name'] + ' info was invalid.')
        else:
            print(x['name'] + ' info was valid.')
#-------------------------------------------------------------------------------------------------------------------------------------------------

vList(people)    
