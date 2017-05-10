'use strict'

var button = document.querySelector(".button");
var body = document.querySelector("body");

function textPrinter () {
    setTimeout( function (){
        var paragraph = document.createElement("p");
        paragraph.textContent = "Two secons elapsed"
        body.appendChild(paragraph);
    }, 2000);

}

button.addEventListener("click", textPrinter)
