'use strict'

var imgList = [
    {src: "Equinox_4.jpg", title: "Equinox 7", description: "whatever"},
    {src: "Equinox_5.jpg", title: "Equinox 8", description: "whatever"},
    {src: "Equinox_6.jpg", title: "Equinox 10", description: "whatever"},
    {src: "Equinox_7.jpg", title: "Equinox 18", description: "whatever"},
    {src: "Equinox_8.jpg", title: "Equinox 15", description: "whatever"},
    {src: "Equinox_10.jpg", title: "Equinox 6", description: "whatever"},
    {src: "Equinox_11.jpg", title: "Equinox 4", description: "whatever"},
    {src: "Equinox_15.jpg", title: "Equinox 8", description: "whatever"},
]

var currentImage = 0;
var mainImage = document.querySelector(".image");
var imageSrc = mainImage.getAttribute("src");


function moveLeft() {
    if (currentImage === 0) {
        currentImage = imgList.length - 1;
    } else {
        currentImage--;
    }
    mainImage.setAttribute("src", imgList[currentImage].src);
}

function moveRight() {
    if (currentImage === imgList.length - 1) {
        currentImage = 0;
    } else {
        currentImage++;
    }
    mainImage.setAttribute("src", imgList[currentImage].src);
}

var buttonLeft = document.querySelector(".left");
var buttonRight = document.querySelector(".right")

buttonRight.addEventListener('click', moveRight);
buttonLeft.addEventListener('click', moveLeft);
