'use strict'
// let url = "http://localhost:3001/";
const submitButton = document.querySelector(".button");

let submitText = function() {
    submitButton.addEventListener("click", function(){
        let shift = document.querySelector(".shift").value;
        let text = document.querySelector(".word").value;
        let message = {
            shift: shift,
            text: text
        };
        submitButton.textContent = "Loading..";
        postAjax(display, message);
    })
}

let postAjax = function(callback, data) {
    const xhr = new XMLHttpRequest();
    xhr.open('POST', "http://localhost:3001/decode", true);
    xhr.setRequestHeader('Content-Type', 'application/json');
    console.log(data);
    xhr.send(JSON.stringify(data));
    xhr.onreadystatechange = function() {
        if (xhr.readyState === 4) {
            if(xhr.status === 200) {
                let resp = JSON.parse(xhr.response);
                console.log(resp);
                callback(resp);
            }
        }
    }
};

let display = function(resp) {
    submitButton.innerHTML = "GO";
    let header = document.createElement("p");
    let decrypted = document.querySelector(".decoded");

    if (resp.status === "ok") {
        resp.forEach(function(el) {
            let decodedword = document.createElement("li");
            decodedword.textContent = el;
            decrypted.appendChild(decodedword);
        })
    } else {
        header.textContent = resp.message;
    }


}

submitText();
