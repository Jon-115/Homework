let playerCard0 = document.getElementById("card0");
let playerCard1 = document.getElementById("card1");
let playerCard2 = document.getElementById("card2");
let playerCard3 = document.getElementById("card3");
let playerCard4 = document.getElementById("card4");
let playerCard5 = document.getElementById("card5");
let playerCard6 = document.getElementById("card6");
let playerCard7 = document.getElementById("card7");
let playerCard8 = document.getElementById("card8");
let playerCard9 = document.getElementById("card9");
let playerCard10 = document.getElementById("card10");
let playerCard11 = document.getElementById("card11");

//if card from a deck is exposed that card value is = "O"
// if card is matched it is ="M"
firstClicked = ''
secondClicked = ''
newGame();
cardDeck1 = [{"value": '8',"8":"-", 'position': 0, 'src':"./assests/8_of_diamonds.png"}, {"value": '9',"9":"-", 'position': 1, 'src':"./assests/9_of_diamonds.png"},{"value": '10',"10":"-", 'position': 2, 'src':"./assests/10_of_diamonds.png"},{"value": 'j',"j":"-", 'position': 3, 'src': './assests/jack_of_diamonds.png}'},{"value": 'q',"q":"-", 'position': 4, 'src': './assests/queen_of_diamonds.png'},{"value": 'k',"k":"-", 'position': 5, 'src': './assests/king_of_diamonds.png'}, {"value": '8',"8":"-", 'position': 6, 'src':"./assests/8_of_diamonds.png"}, {"value": '9',"9":"-", 'position': 7, 'src':"./assests/9_of_diamonds.png"},{"value": '10',"10":"-", 'position': 8, 'src':"./assests/10_of_diamonds.png"},{"value": 'j',"j":"-", 'position': 9,'src': './assests/jack_of_diamonds.png}'},{"value": 'q',"q":"-", 'position': 10, 'src': './assests/queen_of_diamonds.png'},{"value": 'k',"k":"-", 'position': 11, 'src': './assests/king_of_diamonds.png'}]
// cardDeck2 = [{"8":"-", 'position': index, 'src':"/assests/8_of_diamonds.png"}, {"9":"-", 'position': index},{"10":"-", 'position': index},{"j":"-", 'position': index},{"q":"-", 'position': index},{"k":"-", 'position': index}]
function cardClick(index) {
    let playerCard = document.getElementById("card" + index);
    console.log(cardDeck1.length)
   
    for(i = 0;i<cardDeck1.length;i++) {
        if(cardDeck1[i]['position']== index){
            // console.log(cardDeck1[i]['position'])
            playerCard.src = cardDeck1[i]['src']
            firstClicked = cardDeck1[i]['value']
            // console.log(firstClicked)
        }
        else if(cardDeck1[i]['position']== index) {
            playerCard.src = cardDeck1[i]['src']
            secondClicked = cardDeck1[i]['value']
        }
    }
    // && firstClicked == ''
    
}

function checkMatch() {

}


function newGame(){
    let randomArray = [0,1,2,3,4,5,6,7,8,9,10,11]
    console.log(randomArray)
    randomArray.sort(function(){return 0.5 - Math.random()});
    console.log("This should be random" + randomArray)
    for (let index = 0; index < randomArray; index++) {
        cardDeck1[index]['position'] = randomArray[index]
    }
}

