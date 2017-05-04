'use strict'

var newListContent = ['apple', 'banana', 'cat', 'dog'];

var listElements = document.querySelectorAll("li");
for (var i = 0, j = 0; i < listElements.length, j < newListContent.length; i++, j++) {
    listElements[i].textContent = newListContent[j];
}
