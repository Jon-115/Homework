
function speak(word) {

    let letters = new Map ([ ['A', 4],['E',3],['G',6],['I',1],['O',0],['S',5],['T',7] ]);

    word = word.toUpperCase();
    word = word.split("");

    let newWord = ""
    for (let i = 0; i < word.length; i++) {
        if (letters.has(word[i])) {
            newWord = newWord + letters.get(word[i]);
        }
        else {
            newWord = newWord + word[i];
        }
    }
    console.log(newWord.toLowerCase());
}

speak('car');