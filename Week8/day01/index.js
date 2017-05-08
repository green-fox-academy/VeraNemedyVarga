'use strict';
var test = require('tape');

// Length sould al be 9
// [0,0,0,4,5,6,7,8,9] => ok
// [9,0,0,4,5,6,7,8,9] => Should fail
// [1,2,3,4,5,6,7,8,9] => ok
// [2,1,3,4,5,6,7,8,9] => ok
// [9,8,7,6,5,1,2,4,9] => Should fail
// [9,8,7,6,5,1,2,4,'u'] => Shold fail (non integer)
var completeList = [1,2,3,5,5,6,7,8,9];
var differentOrder = [9,8,7,6,5,4,3,2,1];


function lengthValidator (input) {
    if (completeList.length === 9) {
        return true;
    }
};

function ignoreOrdervalidator(input) {
    if (completeList === differentOrder);
    return true;
}

test('Tests if there are nine numbers in list', function (t) {
    t.equal(lengthValidator(completeList), true);
    t.end();
});

test('Order does not count', function(t) {
    t.deepEqual(ignoreOrdervalidator(completeList, differentOrder), true);
    t.end();
})
