'use strict';

var lineCount = 6;

// Write a program that draws a
// square like this:
//
//
// %%%%%
// %   %
// %   %
// %   %
// %   %
// %%%%%
//
// The square should have as many lines as lineCount is

console.log("%".repeat(lineCount - 1));
for (var i = 0; i < lineCount - 2; i++) {
    console.log("%   %")
}
console.log("%".repeat(lineCount - 1));
