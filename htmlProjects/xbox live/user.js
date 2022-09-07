

const createUser = () => {
    fetch("https://random-data-api.com/api/v2/users?size=100")
      .then((response) => {
        return response.json();
      })
      .then((userData) => {
        for (let i = 0; i < 100; i++) {
        //console.log(userData[i]);
        let userTitle = document.createElement('h5')                                // GrandChild
        userTitle.classList.add('card-title')
        userTitle.appendChild(document.createTextNode(userData[i].username))
        //console.log(userTitle.innerText)
        const cIndex = document.getElementById('temp')

        let userOverview = document.createElement('p')                              // GrandChild
        userOverview.classList.add('card-text')
        userOverview.appendChild(document.createTextNode('Hi, my name is ' + userData[i].first_name + ' ' + userData[i].last_name + '. I am a ' + userData[i].employment.title + '.'))

        let userButton = document.createElement('button')                           // GrandChild
        userButton.classList.add('btn')
        userButton.title = 'Name: ' + userData[i].first_name + ' ' + userData[i].last_name + '\nRegion: ' + userData[i].address.country + ', ' + userData[i].address.state + '\nSubscription: ' + userData[i].subscription.plan
        userButton.appendChild(document.createTextNode("More Info"))

        let cardBody = document.createElement('div')                                // Parent
        cardBody.classList.add('card-body')
        cardBody.append(userTitle)
        cardBody.append(userOverview)
        cardBody.append(userButton)
        //console.log(cardBody.innerHTML)

        let cardImage = document.createElement('img')                                // Uncle
        cardImage.classList.add('card-img-top')
        cardImage.src = userData[i].avatar

        let cardBox = document.createElement('div')                                   // GrandParent
        cardBox.classList.add('card')
        cardBox.append(cardImage)
        cardBox.append(cardBody)

        titlecard = document.getElementById('main')
        // titlecard.insertAdjacentElement(cardBox,cIndex)
        titlecard.append(cardBox)
        } 
    }); 
  };









  




