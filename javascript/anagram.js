// function sortList(word) 
// {
//     word = word.toLowerCase();
//     word = word.split("");
//     word = word.sort();
//     console.log(word);
//     return word;
// }

function sortWord(word) {
    word = word.toLowerCase();
    word = word.split("");
    let wordMap = new Map();
    for (let i = 0; i < word.length; i++) {
        if (wordMap.has(word[i])) {
            wordMap.set(word[i],wordMap.get(word[i]) + 1);
        }
        else{
            wordMap.set(word[i],1);
        }
    }
    return wordMap;
}

function isAnagram(word1,word2) 
{
    if (word1.length != word2.length) {
        return "is not an Anagram"
    }
    
    word1 = sortWord(word1);
    word2 = sortWord(word2);
    
    // word1 = word1.toString();
    // word2 = word2.toString();

    console.log(word1);
    console.log(word2);


    if (word1 === word2) {
        return "is an Anagram";
    } 
    else if (word1 !==  word2) {
        return "is not an Anagram";
    }
}

console.log(isAnagram('silent','listen'));
