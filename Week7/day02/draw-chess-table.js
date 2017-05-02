// Create a program that draws a chess table like this
//
// % % % %
//  % % % %
// % % % %
//  % % % %
// % % % %
//  % % % %
// % % % %
//  % % % %
//

for (var i = 0; i < 8; i++) {
    if (i % 2 === 0) {
        console.log(" %".repeat(4));
    } else if (i % 2 !== 0) {
        console.log(" " + " %".repeat(4))
    }
}
