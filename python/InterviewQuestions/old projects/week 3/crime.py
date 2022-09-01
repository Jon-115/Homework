houseList = [{
    "name": "Bob",
    "distance": 1.2,
    "crimes_committed": 1,
    "address": "4325 Birch St"
},
{
    "name": "May",
    "distance": 0.3,
    "crimes_committed": 3,
    "address": "8903 Trolley St"
},
{
    "name": "Tyler",
    "distance": 0.8,
    "crimes_committed": 0,
    "address": "2348 Magnolia Dr"
},
{
    "name": "Reggie",
    "distance": 0.5,
    "crimes_committed": 1,
    "address": "3478 Seminole Ln"
},
{
    "name": "Seth",
    "distance": 3.2,
    "crimes_committed": 0,
    "address": "9803 Azul St"
},
{
    "name": "Ray",
    "distance": 2.9,
    "crimes_committed": 0,
    "address": "3467 Frost St"
},
{
    "name": "Kim",
    "distance": 0.1,
    "crimes_committed": 0,
    "address": "7893 Daisy Ln"
},
{
    "name": "Lisa",
    "distance": 1.2,
    "crimes_committed": 1,
    "address": "2345 Gale St"
},
{
    "name": "Ashley",
    "distance": 1.5,
    "crimes_committed": 5,
    "address": "6783 Sycamore St"
},
{
    "name": "Turner",
    "distance": 4.3,
    "crimes_committed": 1,
    "address": "8923 Pecan Ln"
},
]


def search(houses: list) -> str:
    newList = []
    address = []
    for x in houses:
        if x['distance'] <= 2:
            newList.append(x)
        
    for y in range(len(newList)):
        for x in range(len(newList)-1-y):
            if newList[x]['crimes_committed'] < newList[x+1]['crimes_committed']:
                temp = newList[x]
                newList[x] = newList[x+1]
                newList[x+1]= temp
            elif newList[x]['crimes_committed'] == newList[x+1]['crimes_committed']:
                if newList[x]['distance'] > newList[x+1]['distance']:
                    temp = newList[x]
                    newList[x] = newList[x+1]
                    newList[x+1]= temp
   
    for x in newList:
        address.append(x['address'])

    return address

print(search(houseList))
#search(houseList)