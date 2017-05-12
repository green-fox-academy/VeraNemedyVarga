'use strict'
var ipzandraa= "http://10.27.99.62:8080/posts";

let getData = function() {
    var httpRequest = new XMLHttpRequest();
    var url = "https://time-radish.glitch.me/posts";
    httpRequest.open('GET', ipzandraa, true);
    httpRequest.setRequestHeader('Accept', 'application/json');

    httpRequest.onreadystatechange = function() {
        if (httpRequest.readyState === 4) {
            if (httpRequest.status === 200) {
                var resp = JSON.parse(httpRequest.response);
                var posts = resp.posts
                // console.log(posts)

                generatePost(posts);
            }
        }
    };
    httpRequest.send(null);
};

var generatePost = function (posts) {
    posts.forEach( function(post) {
        var title = post.title;
        var href = post.href;
        var score = post.score;
        var post = document.querySelector(".post");
        var postClone = post.cloneNode(true);
        var mainContent = document.querySelector(".main")
        var upvoteButton = postClone.querySelector(".upvote");
        var downvoteButton = postClone.querySelector(".downvote");
        var scorePoints = postClone.querySelector(".scores");
        scorePoints.textContent = score;
        var threadTitle = postClone.querySelector(".threadtitle");
        var threadcontent = postClone.querySelector(".threadcontent");
        var modifyButton = postClone.querySelector(".modify");
        var removeButton = postClone.querySelector(".remove");
        var owner = postClone.querySelector(".owner");
        mainContent.appendChild(postClone);
        threadTitle.textContent = title;
        // owner.textContent = href;
        threadTitle.addEventListener("click", threadTitle.setAttribute("href", href));

        // upvoteButton.addEventListener("click", );

    });
};

let postData = function() {
    var httpRequest = new XMLHttpRequest();
    var url = "https://time-radish.glitch.me/posts";
    httpRequest.open('POST', ipzandraa, true);
    httpRequest.setRequestHeader('Accept', 'application/json', 'Content-Type', 'application/json');

    httpRequest.onreadystatechange = function() {
        if (httpRequest.readyState === 4) {
            if (httpRequest.status === 200) {
                var resp = JSON.parse(httpRequest.response);
                var posts = resp.posts
                // console.log(posts)

                generatePost(posts);
            }
        }
    };
    httpRequest.send(null);
};

getData();
