'use strict'

var asteroidList = document.querySelector("ul");

var greenFox = document.createElement("li");
greenFox.textContent = "The Green Fox";
asteroidList.appendChild(greenFox);

var lampLighter = document.createElement("li");
lampLighter.textContent = "The Lamplighter";
asteroidList.appendChild(lampLighter);

var heading = document.createElement("h1");
heading.textContent = "I can add elements to the DOM!"
var body = document.querySelector("body");
body.insertBefore(heading, asteroidList);

var img = document.createElement("img");
img.src = "puppyteeth01.png";
var container = document.querySelector("div");
container.appendChild(img);
