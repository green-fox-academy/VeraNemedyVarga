'use strict'

var img = document.querySelector("img");
console.log(img.getAttribute("src"));
img.setAttribute("src", "vera.jpg");

var link = document.querySelector("a");
link.setAttribute("href", "https://www.greenfoxacademy.com/");

var firstButton = document.querySelectorAll("button")[0];
firstButton.disabled = true;
firstButton.textContent = "Don't click me!"
