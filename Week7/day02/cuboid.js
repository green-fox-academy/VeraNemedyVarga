'use strict';

// Write a program that stores 3 sides of a cuboid as variables (floats)
// The program should write the surface area and volume of the cuboid like:
//
// Surface Area: 600
// Volume: 1000

var width = 23;
var height = 10;
var depth = 40;

var surface = 2 * (width * height + width * depth + height * depth);
var volume = width * height * depth;

console.log("Surface Area: " + surface);
console.log("Volume: " + volume);
