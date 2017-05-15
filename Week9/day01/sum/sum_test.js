'use strict';

let test = require('tape');
let summing = require('./sum');


test('tests for empty list, returns zero', function (t) {
    t.equal(summing.sum([]), 0);
    t.end();
})

test('tests for one element list, returns element', function(t) {
    t.equal(summing.sum([8]), 8);
    t.end();
})

test('returns sum of numbers in list', function (t) {
    t.equal(summing.sum([2, 3, 4]), 9);
    t.end();
})

test('returns error message for null in list', function(t) {
    t.throws(function(){
        throw summing.sum(null)
    }, Error, 'parameter is not a list');
    t.end();
})

test('tests for string, throws error message', function(t) {
    t.throws(function(){
        throw summing.sum('zsolt')
    }, Error, 'parameter is not a list');
    t.end();
})
