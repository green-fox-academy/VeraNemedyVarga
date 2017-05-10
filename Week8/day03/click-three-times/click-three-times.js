'use strict'

var button = document.querySelector(".button");
var body = document.querySelector("body");
var counter = 0;
var loadedWindow = false;

function threeClick() {
    counter += 1;
    console.log(counter);
    console.log(loadedWindow);
    if (counter >= 3 && loadedWindow === true) {
        var paragraph = document.createElement("p");
        paragraph.textContent = "5 seconds ellapsed and clicked 3 times";
        body.appendChild(paragraph);
        counter = 0;
    }
}
window.addEventListener('load', setTimeout(function () {
    loadedWindow = true;
}, 5000))
button.addEventListener("click", threeClick)
