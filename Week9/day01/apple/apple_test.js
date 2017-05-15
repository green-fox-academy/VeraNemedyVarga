let test = require('tape');
let apple = require('./apple');

test('return "apple"', function(t){
    var actual = apple.getApple();
    var expected = "apple";
    t.equal(actual, expected);
    t.end();
});
