// Create a function that takes a string and a letter, than returns a list that contains all the indexes where the letter occured in the string.

let letterIndexes = function (somestr, letter) {
    let indexes = [];
    for (let i = 0; i < somestr.length; i++) {
        if (somestr[i] === letter) {
            // indexes += i;
            indexes.push(i);
        }
    }
    // indexes = indexes.split('');
    return indexes;
}

console.log(letterIndexes("terrier", "r"));
