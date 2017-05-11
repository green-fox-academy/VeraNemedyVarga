
var body = document.querySelector("body");
var container = document.querySelector(".container");

var httpRequest = new XMLHttpRequest();
httpRequest.open('GET', "http://api.giphy.com/v1/gifs/trending?api_key=dc6zaTOxFJmzC", true);
httpRequest.setRequestHeader('Content-Type', 'text/html');



var imageFinder = function () {
    if (httpRequest.readyState === 4) {
        if (httpRequest.status === 200) {
            var resp = JSON.parse(httpRequest.response);
            var data = resp.data;
            console.log(data);

            for (let i = 0; i < 16; i++) {
                var url = data[i].images.fixed_width_small_still.url;
                var gifurl = data[i].images.fixed_width_small.url;
                console.log(url);
                imageDisplay(url, gifurl);
            }
        } else {
            alert('There was a problem with the request')
        }
    }
};

var imageDisplay = function(url, gifurl) {
    var image = document.createElement("img");
    container.appendChild(image);
    image.style.display = "inline-block";
    container.style.width = "500px";
    container.style.margin = 'auto';
    image.style.padding = "10px";
    image.setAttribute("src", url);
    var clicked = false;
    image.addEventListener("click", function(){
        clicked = true;
        if (clicked) {
            this.src = gifurl;
        };
        image.addEventListener("click", function() {
            clicked = false;
            if (clicked === false) {
                this.src = url;
            }
        })
    });
}


httpRequest.onreadystatechange = imageFinder;
httpRequest.send(null);
