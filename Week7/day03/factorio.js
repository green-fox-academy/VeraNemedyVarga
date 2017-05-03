'use strict';
// - Create a function called `factorio`
//   that returns it's input's factorial

function factorio(num) {
    var result = 0;
    if (num <= 1 || num === 0) {
        return 1;
    } else {
        result = num * (factorio(num - 1));
    }
    return result;
}

console.log(factorio(4))
