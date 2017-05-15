let test = require('tape');
let ana = require('./anagram');

test('tests for anagram strings', function(t) {
    t.equal(ana('BALE', 'ABEL'), true);
    t.end();
});

test('test for same but multiple occurence of letters in one string', function(t) {
    t.equal(ana('BALE', 'AABEL'), false);
    t.end();
})

test('test for anagrams of upper-lowercase mix words', function(t) {
    t.equal(ana("Bale", "ABEL"), true);
    t.end();
});

test('test for not string type parameter', function(t) {
    t.throws(function() {
        throw ana(34, 'halo');
    }, Error, "first parameter must be 'string'");
    t.end();
});

test('test for not string type parameter', function(t) {
    t.throws(function() {
        throw ana('halo', [5]);
    }, Error, "second parameter must be 'string'");
    t.end();
});
