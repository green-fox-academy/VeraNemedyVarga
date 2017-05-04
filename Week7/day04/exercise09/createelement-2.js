'use strict'

var asteroid = document.querySelector("ul");
var king = document.querySelector("li");
asteroid.removeChild(king, asteroid);

for (var i = 0; i < 3; i++) {
    var listElement = document.createElement("li");
    listElement.textContent = "The Fox";
    asteroid.appendChild(listElement);
}
