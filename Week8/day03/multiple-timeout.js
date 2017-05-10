'use strict';

// Write a program that prints the following fruits:
// apple -> immediately
// pear -> after 1 seconds
// melon -> after 3 seconds
// grapes -> after 5 seconds

var fruitlist = ["apple", "pear", "melon", "grapes"]
var timing = [0, 1000, 3000, 5000]

function fruitPrinter(fruit, timing) {
    setTimeout (function () {
        console.log(fruit);
    }, timing)
}

fruitPrinter("apple", 0)
fruitPrinter("pear", 1000)
fruitPrinter("melon", 3000)
fruitPrinter("grapes", 5000)
