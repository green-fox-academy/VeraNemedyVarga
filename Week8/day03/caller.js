'use strict';

// Implement the selectLastEvenNumber function that takes an array and callback,
// it should call the callback immediately with the last even number on the array


function printNumber(num) {
  console.log(num);
}

function selectLastEvenNumber(numbers, callback) {
    numbers = numbers.filter(function (num) {
        return num % 2 === 0
    });callback(numbers.pop())
};


selectLastEvenNumber([2, 5, 7, 8, 9, 11], printNumber); // should print 8
