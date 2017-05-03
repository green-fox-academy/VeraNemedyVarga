'use strict';
// - Write a function called `sum` that sum all the numbers until the given parameter
// - The function should return the result

function sum(endNum) {
    var result = 0;
    for (var i = 1; i < endNum + 1; i++) {
        result += i;
    }
    return result;
}

console.log(sum(4));
