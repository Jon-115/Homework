const tooltipTriggerList = document.querySelectorAll('[data-bs-toggle="tooltip"]')
const tooltipList = [...tooltipTriggerList].map(tooltipTriggerEl => new bootstrap.Tooltip(tooltipTriggerEl))


const createUser = () => {
    fetch("https://random-data-api.com/api/v2/users?size=1")
      .then((response) => {
        return response.json();
      })
      .then((userData) => {
        //console.log(userData.name);
        let userTitle = document.createElement('h5')                                // GrandChild
        userTitle.classList.add('card-title')
        userTitle.appendChild(document.createTextNode(userData.username))
        //console.log(userTitle.innerText)
        const cIndex = document.getElementById('main')

        let userOverview = document.createElement('p')                              // GrandChild
        userOverview.classList.add('card-text')
        userOverview.appendChild(document.createTextNode('Hi my name is ' + userData.first_name + ' ' + userData.last_name + ' I am a ' + userData.employment.title))

        let userButton = document.createElement('button')                           // GrandChild
        userButton.classList.add('btn')
        userButton.appendChild(document.createTextNode("More Info"))

        let cardBody = document.createElement('div')                                // Parent
        cardBody.classList.add('card-body')
        cardBody.append(userTitle)
        cardBody.append(userOverview)
        cardBody.append(userButton)
        //console.log(cardBody.innerHTML)

        let cardImage = document.createElement('img')                                // Uncle
        cardImage.classList.add('card-img-top')
        cardImage.src = userData.avatar

        let cardBox = document.createElement('div')                                   // GrandParent
        cardBox.classList.add('card')
        cardBox.append(cardImage)
        cardBox.append(cardBody)

        document.body.insertBefore(cardBox,cIndex)
    });
  };

function getUsers() {
  for (let i = 0; i < 10; i++) {
    createUser();
  }
  document.getElementById('userButton').remove();
}







  




