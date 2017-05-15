let test = require('tape');
let apple = require('./apple');

test('return "apple"', function(t){
    t.equal('apple', apple.getApple());
    t.end();
});
