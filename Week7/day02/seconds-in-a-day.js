'use strict';

var currentHours = 14;
var currentMinutes = 34;
var currentSeconds = 42;

// Write a program that prints the remaining seconds (as an integer) from a
// day if the current time is represented by these variables
var currentTimeInSeconds = currentHours * 3600 + currentMinutes * 60 + currentSeconds;
var secondsInADay = 24 * 3600;
var remainingSeconds = secondsInADay - currentTimeInSeconds;
console.log(remainingSeconds);
