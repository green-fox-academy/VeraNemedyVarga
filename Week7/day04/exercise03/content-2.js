'use strict'

var paragraph = document.querySelectorAll('p');
var lastPContent = paragraph[paragraph.length -1].textContent;
console.log(lastPContent);
for (var p = 0; p < paragraph.length; p++) {
    paragraph[p].textContent = lastPContent
    console.log(paragraph[p].textContent);
}
