'use strict'

var firstPContent = document.querySelectorAll('p')[0].textContent;
document.querySelector(".output1").textContent = firstPContent;
// document.querySelector(".output2").textContent = document.body.childNodes[0].textContent;
var firstPWithStrong = document.querySelectorAll('p')[0].innerHTML;
document.querySelector(".output2").innerHTML = firstPWithStrong
