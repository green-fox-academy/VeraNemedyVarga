'use strict'

var express = require('express');
let app = express();


app.get('/', function(req, res) {
    res.sendFile(__dirname + '/index.html');
    app.use('/assets/', express.static('assets'));
});

app.get('/doubling', function(req, res) {
    let queryInupt = req.query.input;
    if (typeof queryInupt === undefined) {
        res.send({
            error: "Please provide an input"
        })
    } else {
        res.send({
            received: queryInupt,
            result: queryInupt * 2
        })
    }
});

app.get('/greeter', function(req, res) {
    var name = req.params.name;
    var title = req.params.title;
    if (name == undefined || title == undefined){
        res.send({
            error: "Please provide a name!"
        });
    } else if (name == "Petike", title == "student"){
        res.send({
            welcome_message: "Oh, hi there Petike, my dear student!"
        })
    }
});


app.listen(8080);

// Create a GET /greeter endpoint
// that receives a query parameter name=Petike&title=student
// and responds with an awesome greeting json object:
// {
//   "welcome_message": "Oh, hi there Petike, my dear student!"
// }
// if e.g. no name (or title) is provided:
// {
//   "error": "Please provide a name!"
// }
