const dealerHand = document.getElementById("dealer_label");
const playerHand = document.getElementById("player_label");
const deck = [];
let dPoints = 0;
let pPoints = 0;
let pimage = 3;
let dimage = 2;
let gameover = false;
let playerCount = 0;
let dealerCount = 0
const suits = ["hearts", "spades", "clubs", "diamonds"];
const ranks = ["ace", 2, 3, 4, 5, 6, 7, 8, 9, 10, "jack", "queen", "king"];
const makeDeck = (rank, suit) => {
  const card = {
    rank: rank,
    suit: suit,
    pointValue: rank > 10 ? 10 : rank,
  };
  deck.push(card);
};
//--------------------------------------------------------------------------------------------------------------
function shuffle(deck) {
  let i = deck.length, ri;

  while (i != 0) {
    ri = Math.floor(Math.random()*i);
    i--;

    [deck[i], deck[ri]] =  [deck[ri], deck[i]];
  }
}
//--------------------------------------------------------------------------------------------------------------
function getDeck() {
for (let suit of suits) {
  for (const rank of ranks) {
    makeDeck(rank, suit);
  }
  shuffle(deck)
}
}
//--------------------------------------------------------------------------------------------------------------
function dealerCard(id) {
  newCard = deck.shift();
  r = newCard.rank  // shorthand for rank
  s = newCard.suit  // shorthand for suit
  document.getElementById(id).src = './images/' + r + '_of_' + s + '.png';
  dPoints = calculatePoints(r, dPoints);
  dealerHand.innerText = 'Dealer: ' + dPoints + ' Wins: ' + dealerCount;
}
//--------------------------------------------------------------------------------------------------------------
function playerCard(id) {
  newCard = deck.shift();
  r = newCard.rank  // shorthand for rank
  s = newCard.suit  // shorthand for suit
  document.getElementById(id).src = './images/' + r + '_of_' + s + '.png';
  pPoints = calculatePoints(r, pPoints);
  playerHand.innerText = 'Player: ' + pPoints + ' Wins: ' + playerCount;
}
//--------------------------------------------------------------------------------------------------------------
function resetimg() {
  document.getElementById('p3').src = '';
  document.getElementById('p4').src = '';
  document.getElementById('p5').src = '';
  document.getElementById('d2').src = '';
  document.getElementById('d3').src = '';
  document.getElementById('d4').src = '';
  document.getElementById('d5').src = '';
}
//--------------------------------------------------------------------------------------------------------------
function dealCards() { // Linked to the 'deal' button
  resetimg();
  gameover = false;

  getDeck();
  dealerCard('d1');
  // dealerCard('d2');
  playerCard('p1');
  playerCard('p2');


  checkPoints('deal');
  console.log(dPoints,pPoints);
} 
//--------------------------------------------------------------------------------------------------------------
function hitCard() { // Linked to the 'hit' button
  playerCard('p' + pimage);
  checkPoints('hit');
  console.log(dPoints,pPoints);
  pimage += 1
}
//--------------------------------------------------------------------------------------------------------------
function stand() { // Linked to the 'stand' button
  while (gameover == false) {
    dealerCard('d' + dimage);
    checkPoints('stand');
    dimage += 1
  }
  
}
//--------------------------------------------------------------------------------------------------------------
function calculatePoints(rank, points) {
  if (rank == 'ace') {
    points += 11;
  }
  else if (rank == "jack" || rank == "queen" || rank == "king") {
    points += 10;
  }
  else {
    points += rank;
  }
  return points
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
      else {
        alert('Dealer busted. You Won!')
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
function restart(winner) {
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