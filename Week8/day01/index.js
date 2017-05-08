'use strict';
var test = require('tape');

// Length sould al be 9
// [0,0,0,4,5,6,7,8,9] => ok
// [9,0,0,4,5,6,7,8,9] => Should fail
// [1,2,3,4,5,6,7,8,9] => ok
// [2,1,3,4,5,6,7,8,9] => ok
// [9,8,7,6,5,1,2,4,9] => Should fail
// [9,8,7,6,5,1,2,4,'u'] => Shold fail (non integer)
var completeList = [1, 2, 3, 5, 5, 6, 7, 8, 9];
var differentOrder = [9, 8, 7, 6, 5, 4, 3, 2, 1];
var stringList = ['w', 2, 3, 4, 5, 6, 7, 8, 9];
var incompleteList = [1, 2, 3, 4, 5];
var multipleOccurance = [1, 2, 1, 3, 4, 5, 6, 7, 8];

function validator (input) {
    for (var index = 0; index < input.length; index++) {
        if (input[index].typeOf !== 'String' && input.length === 9 && input.sort()[index] !== input.sort()[index+1]) {
        return true;
        }
    }
};

test('Tests if there are nine numbers in list', function (t) {
    t.notEqual(validator(incompleteList), true);
    t.end();
});

test('No string allowed', function(t) {
    t.notEqual(validator(stringList), false);
    t.end();
});

test('More than one occurence of a number', function(t){
    t.equal(validator(multipleOccurance), true);
    t.end();
});
