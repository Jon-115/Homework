deck = ['8','9','10','jack','queen','king','8','9','10','jack','queen','king']
count = 0
gameOver = false
card1 = ''
card2 = ''
i1 = 0
i2 = 0

function cardClick(index) {
    // console.log(deck)
    if (count % 2 == 0) {
        document.getElementById('card'+index).src = './assests/' + deck[index] +'_of_diamonds.png'
        card1 = deck[index]
        i1 = index
        count++
    }
    else if (count % 2 != 0  &&  index != i1) {
        document.getElementById('card'+index).src = './assests/' + deck[index] +'_of_diamonds.png'
        card2 = deck[index]
        i2 = index
        checkCards()
        count++
    }
}

function checkCards() {
    console.log(card1+' '+i1)
    console.log(card2+' '+i2)
    if (card1 == card2){
        document.getElementById('card'+i1).src = ""
        document.getElementById('card'+i2).src = ""
        deck.splice(i1,1)
        deck.splice(i2-1,1)
    }
    else if ( deck.length == 0) {
        gameOver = true
        alert('You won')
    }
    else {
        document.getElementById('card'+i1).src = "./assests/cardDown.png"
        document.getElementById('card'+i2).src = "./assests/cardDown.png"
    }
    console.log(deck)
}

function newGame() {
    for (let i = 0; i < 12; i++) {
    document.getElementById('card'+i).src = "./assests/cardDown.png"
    }
    deck = ['8','9','10','jack','queen','king','8','9','10','jack','queen','king'] 
    shuffle() 
}

function shuffle() {
    console.log(deck)
    deck.sort(function(){return 0.5 - Math.random()});
    console.log("this is random deck:"+deck)
}