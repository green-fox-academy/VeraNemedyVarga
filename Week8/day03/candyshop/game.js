'use strict'

var candycreatebutton = document.querySelector(".create-candies");
var buylollipopbutton = document.querySelector(".buy-lollypops");
var candymachinebutton = document.querySelector(".candy-machine");

var candycounter = 1000;
var candy = document.querySelector(".candies");
candy.textContent = candycounter.toString();
candycreatebutton.addEventListener("click", addCandy)

function addCandy() {
    candycounter ++;
    candy.textContent = candycounter.toString();
}

var lollypopcounter = 0;
var lollypop = document.querySelector(".lollypops");
lollypop.textContent = lollypopcounter.toString();
buylollipopbutton.addEventListener("click", buyLollypop)

function buyLollypop() {
    if (candycounter >= 100) {
        lollypopcounter ++;
        lollypop.textContent = "🍭".repeat(lollypopcounter).toString();
        candycounter -= 100;
        candy.textContent = candycounter.toString();
    }
}
