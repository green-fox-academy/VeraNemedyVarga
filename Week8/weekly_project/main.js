'use strict'

let getData = function() {
    var httpRequest = new XMLHttpRequest();
    var url = "https://time-radish.glitch.me/posts";
    httpRequest.open('GET', url, true);
    httpRequest.setRequestHeader('Accept', 'application/json');

    httpRequest.onreadystatechange = function() {
        if (httpRequest.readyState === 4) {
            if (httpRequest.status === 200) {
                var resp = JSON.parse(httpRequest.response);
                var data = resp.data;
                console.log(resp);
            }
        }
    };
    httpRequest.send(null);
}


getData();
