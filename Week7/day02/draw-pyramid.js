'use strict';

var lineCount = 4;
var j = 4;
// Write a program that draws a
// pyramid like this:
//
//
//    *
//   ***
//  *****
// *******
//
// The pyramid should have as many lines as lineCount is

for (var i = 1, j = 4; i < lineCount * 2 + 1, 0 < j; i += 2, j--) {{
        console.log(' '.repeat(j) + '*'.repeat(i));
    }
}
