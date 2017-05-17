'use strict'

var express = require('express');
let app = express();


app.get('/', function(req, res) {
    res.sendFile(__dirname + '/index.html');
    app.use('/assets/', express.static('assets'));
});

app.get('/doubling', function(req, res) {
    let queryInput = req.query.input;
    if (req.query.input === undefined) {
        res.send({
            error: "Please provide an input!"
        })
    } else {
        console.log(req.query);
        res.send({
            received: queryInput,
            result: queryInput * 2
        })
    }
});

app.get('/greeter', function(req, res) {
    var name = req.query.name;
    var title = req.query.title;
    if (name === undefined){
        res.send({
            error: "Please provide a name!"
        });
    } else if (title === undefined) {
        res.send({
            error: "Please provide a title!"
        });
    } else {
        res.send({
            welcome_message: "Oh, hi there " + name + ", my dear " + title + "!"
        })
    }
});

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

app.listen(8080);
