'use strict'
const express = require('express');
const bodyparser = require('body-parser');
const mysql = require('mysql');
const app = express();
app.use(bodyparser.json());
app.use('/assets/', express.static('assets'));

const conn = mysql.createConnection({
    host: 'localhost',
    user: 'root',
    password: 'root',
    database: 'caesar'
});

let response = {
    status: "error",
    message: "Thank you"
};

app.get('/', function(req, res) {
    res.sendFile(__dirname + '/index.html')
});


let caesarShift = function (text, shift) {
	var result = "";
	for (var i = 0; i < text.length; i++) {
		var c = text.charCodeAt(i);
		if      (65 <= c && c <=  90) result += String.fromCharCode((c - 65 + shift) % 26 + 65);  // Uppercase
		else if (97 <= c && c <= 122) result += String.fromCharCode((c - 97 + shift) % 26 + 97);  // Lowercase
		else                          result += text.charAt(i);  // Copy
	}
	return result;
}

app.post('/decode', function(req, res) {
    console.log("valami");
    console.log(req.body);
    if(req.body.shift < -25 || req.body.shift > 25) {
        response = {
            status: "error",
            error: "Shift is out of bound"
        }
        res.send(response);

    } else {
        response =   {
            status: "ok",
            text: caesarShift(req.body.text, req.body.shift)
        }
        res.send(response);

        conn.query("INSERT INTO words SET ?", [{decrypted: response.text}], function(err, rows) {
            if(err) {
                console.log(err);
                response = {
                    status: "error",
                    error: "Problem with database"
                }
                res.send(response);
            }
        });
        console.log(response)
    }
    //});
});


app.listen(3001, function(){
    console.log("server running");
});
