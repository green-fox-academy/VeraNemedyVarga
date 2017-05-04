'use strict'

var thirdP = document.querySelectorAll('p')[2];
if (thirdP.classList.contains("cat")) {
    alert("YEAH CAT!");
};

var secondP = document.querySelectorAll('p')[1];

var fourthP = document.querySelectorAll('p')[3];
if (fourthP.classList.contains("dolphin")) {
    firstP.textContent = "pear";
};

var firstP = document.querySelectorAll('p')[0];
if (firstP.classList.contains("apple")) {
    thirdP.textContent = "dog";
};

firstP.style.color = "red";
secondP.style.borderRadius = "25%";
