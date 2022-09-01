const dealerHand = document.getElementById("dealer_label");                   // Creation of global variables
const playerHand = document.getElementById("player_label");
let deck = [];
let dPoints = 0;
let pPoints = 0;
let pimage = 3;
let dimage = 2;
let gameover = false;
let playerCount = 0;
let dealerCount = 0;
const suits = ["hearts", "spades", "clubs", "diamonds"];
const ranks = ["ace", 2, 3, 4, 5, 6, 7, 8, 9, 10, "jack", "queen", "king"];
//--------------------------------------------------------------------------------------------------------------
const makeDeck = (rank, suit) => {                                            // Creation of deck of cards
  const card = {
    rank: rank,
    suit: suit,
    pointValue: rank > 10 ? 10 : rank,
  };
  deck.push(card);
};
//--------------------------------------------------------------------------------------------------------------
function shuffle(deck) {                                                      // Shuffles deck
  let i = deck.length
  let ri;

  while (i != 0) {
    ri = Math.floor(Math.random()*i);
    i--;

    [deck[i], deck[ri]] =  [deck[ri], deck[i]];
  }
}
//--------------------------------------------------------------------------------------------------------------
function getDeck() {                                                          // Passes parameters of rank and suit
deck = []
for (const suit of suits) {                                                     // of a card
  for (const rank of ranks) {
    makeDeck(rank, suit);
  }
}
shuffle(deck);
}
//--------------------------------------------------------------------------------------------------------------
function dealerCard(id) {                                                      // Gives Dealer his hand
  newCard = deck.shift();
  r = newCard.rank  // shorthand for rank
  s = newCard.suit  // shorthand for suit
  document.getElementById(id).src = './images/' + r + '_of_' + s + '.png';
  dPoints = calculatePoints(r, dPoints);
  dealerHand.innerText = 'Dealer: ' + dPoints + ' Wins: ' + dealerCount;
}
//--------------------------------------------------------------------------------------------------------------
function playerCard(id) {                                                       // Gives Player their hand
  newCard = deck.shift();
  r = newCard.rank  // shorthand for rank
  s = newCard.suit  // shorthand for suit
  document.getElementById(id).src = './images/' + r + '_of_' + s + '.png';
  pPoints = calculatePoints(r, pPoints);
  playerHand.innerText = 'Player: ' + pPoints + ' Wins: ' + playerCount;
}
//--------------------------------------------------------------------------------------------------------------
function resetimg() {                                                           // resets images/cards
  document.getElementById('p3').src = '';
  document.getElementById('p4').src = '';
  document.getElementById('p5').src = '';
  document.getElementById('d2').src = '';
  document.getElementById('d3').src = '';
  document.getElementById('d4').src = '';
  document.getElementById('d5').src = '';
}
//--------------------------------------------------------------------------------------------------------------
function faceDown(num) {
  document.getElementById('d' + num).src = './images/card_of_down.png';
}
//--------------------------------------------------------------------------------------------------------------
function dealCards() {                                                        // Linked to the 'deal' button and starts the Gamse
  if (pPoints == 0) {
    resetimg();                                                                
  gameover = false;

  getDeck();
  //console.log(deck.length)
  //console.log(deck[0],deck[1],deck[2])
  dealerCard('d1');
  faceDown(2);
  
  playerCard('p1');
  playerCard('p2');
  
  checkPoints('deal');
  }
} 
//--------------------------------------------------------------------------------------------------------------
function hitCard() {                                                          // Linked to the 'hit' button
  if (gameover == false){
    playerCard('p' + pimage);
    pimage += 1;
    checkPoints('hit');
  }
}
//--------------------------------------------------------------------------------------------------------------
function stand() {                                                            // Linked to the 'stand' button
  while (gameover == false) {
    dealerCard('d' + dimage);
    dimage += 1;
    checkPoints('stand');
  }
  
}
//--------------------------------------------------------------------------------------------------------------
function calculatePoints(rank, points) {                                       // Calculates Points of both parties
  if (rank == 'ace') {
    points += 11;
  }
  else if (rank == "jack" || rank == "queen" || rank == "king") {
    points += 10;
  }
  else {
    points += rank;
  }
  return points;
}
//--------------------------------------------------------------------------------------------------------------
function checkPoints(code) { // Called by the 3 functions linked to the 3 buttons: dealCards(), hitCard(), stand()
  if (code == 'stay') {                           // Logic block 1
    alert('Dealer has Won')
    restart('dealer')
  }                                               // Logic block 1

  if (code == 'stand') {                          // Logic block 2
    if (dPoints >= 17 && dPoints < 21) {
      if (dPoints > pPoints){
        alert('Dealer has Won')
        restart('dealer')
      }
      else if (dPoints == pPoints) {
        alert('Tie!')
        restart('player')
      }
      else if (dPoints > 21) {
        alert('Dealer busted. You Won!')
        restart('player')
      }
    else if (dimage == 5) {
      alert('Dealer can no longer hit.')
      restart('player')
    }
    }
  }                                             // Logic block 2

  if (code == 'hit') {                          // Logic block 3
    if (dPoints > pPoints) {
      alert('Dealer has Won!')
      restart('dealer')
    }
  }                                             // Logic block 3
  
  if (pPoints == 21) {                          // Logic block 4
    alert('You won!')
    restart('player')
  }
  else if (pPoints > 21) { // Player bust
    alert('Bust!')
    restart('dealer')
  }
  else if (dPoints == 21) {
    alert('Dealer won!')
    restart('dealer')
  }
  else if (dPoints > 21) { // Dealer bust
    alert('The dealer busted. You Won!')
    restart('player')
  }                                            // Logic block 4
}
//--------------------------------------------------------------------------------------------------------------
function restart(winner) {                                                  //restarts the game
  if (winner == 'player') {
    playerCount += 1;
  }
  else {
    dealerCount += 1
  }
  
  gameover = true

  playerHand.innerText = 'Player: ' + pPoints + ' Wins: ' + playerCount;
  dealerHand.innerText = 'Dealer: ' + dPoints + ' Wins: ' + dealerCount;

  dPoints = 0;
  pPoints = 0;
  pimage = 3;
  dimage = 2;
}
//--------------------------------------------------------------------------------------------------------------
