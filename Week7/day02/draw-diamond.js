'use strict';

var lineCount = 7;



// Write a program that draws a
// diamond like this:
//
//
//    *
//   ***
//  *****
// *******
//  *****
//   ***
//    *
//
// The diamond should have as many lines as lineCount is

for (var i = 1, j = 4; i < lineCount * 2 + 1, 0 < j; i += 2, j--) {{
        console.log(' '.repeat(j) + '*'.repeat(i));
    }
}
for (var i = 2, j = 5; i < lineCount * 2 + 1, 0 < j; i++, j-=2) {{
        console.log(' '.repeat(i) + '*'.repeat(j));
    }
}
