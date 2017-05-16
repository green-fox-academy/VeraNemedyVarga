'use strict'

var express = require('express');
let app = express();

app.use(express.static('/assets'));

app.get('/', function(req, res) {
    res.sendFile(__dirname + '/index.html');
});

app.listen(8080);
