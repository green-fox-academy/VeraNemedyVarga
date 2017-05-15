// Write a function, that takes two strings and returns a boolean value based on if the two strings are Anagramms or not.
// Create a test for that.
'use strict'

let anagram = function(str1, str2) {
    if (typeof str1 !== "string") {
        throw new Error("first parameter must be 'string'");
    } else if(typeof str2 !== "string") {
        throw new Error("second parameter must be 'string'");
    } else {
        str1 = str1.toLowerCase();
        str2 = str2.toLowerCase();
        let an1 = str1.split("").sort().join("");
        let an2 = str2.split("").sort().join("");
        return an1 === an2;
    }
}

module.exports = anagram;
