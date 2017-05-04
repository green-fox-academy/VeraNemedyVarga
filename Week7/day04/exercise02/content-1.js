'use strict'

var heading = document.querySelector('h1');
alert(heading.textContent);

var pContent = document.getElementsByTagName('p');
console.log(pContent[0]);
alert(pContent[1].textContent);

heading.textContent = "New Content";
pContent[pContent.length - 1].textContent = pContent[0].textContent;
