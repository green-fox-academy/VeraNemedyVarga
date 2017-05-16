'use strict'

var express = require('express');
let app = express();


app.get('/', function(req, res) {
    res.sendFile(__dirname + '/index.html');
    app.use('/assets/', express.static('assets'));
});

app.get('/doubling', function(req, res) {
    let queryInupt = req.query.input;
    if (queryInupt === '') {
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


app.listen(8080);



// Create a GET /doubling endpoint
// That receives a query parameter: input=15
// And responds with a json object with the doubled amount of the input:
// {
//   "received": 15,
//   "result": 30
// }
// if no input is provided:
// {
//   "error": "Please provide an input!"
// }
