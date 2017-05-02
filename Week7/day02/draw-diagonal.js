'use strict';

var lineCount = 6;


// Write a program that draws a
// square like this:
//
//
// %%%%%
// %%  %
// % % %
// %  %%
// %   %
// %%%%%
//
// The square should have as many lines as lineCount is

for (var i = 0; i < lineCount; i++) {
    if (i === 0 || i === lineCount - 1) {
        console.log("%".repeat(lineCount - 1))
    } else if (i === lineCount - 2) {
        console.log("%" + " ".repeat(i - 1) + " ".repeat(lineCount - i - 2) + "%");
    } else {
        console.log("%" + " ".repeat(i - 1) + "%" + " ".repeat(lineCount - i - 3) + "%");
    }
}
