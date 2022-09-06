import requests

userList = []

for x in range(10):

    response = requests.get('https://random-data-api.com/api/v2/users?size=1')
    response = response.json()
    #print(response)
    fullName = (response['first_name'],response['last_name'])
    userList.append(fullName)

for x in range(len(userList)):
    for y in range(len(userList)-1-x):
        if userList[y][1] > userList[y+1][1]:
            temp = userList[y+1]
            userList[y+1] = userList[y]
            userList[y] = temp

print(userList)





