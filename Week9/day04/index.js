const mysql = require('mysql');
const express = require('express');
const app = express();

var conn = mysql.createConnection({
    host: 'localhost',
    user: 'root',
    password: 'root',
    database: 'bookstore'
})

conn.connect(function(err){
  if(err){
    console.log("Error connecting to Db");
    return;
  }
  console.log("Connection established");
});


let tabledrawer = function(rows) {
    let table = "<table>";
    let heading = Object.keys(rows[0]);
    heading.forEach(function(key) {
        table += "<th>" + key + "</th>";
    });
    table += "</tr>"
    rows.forEach(row => {
        table += "<tr>";
        for (key in row) {
            table +="<td>" + row[key] + "</td>"
        }
        table += "</tr>";
    })
    table += "</table>";
    return table;
}


app.get('/', function get(req, res) {
    var result = "";
    conn.query("SELECT book_mast.book_name, purch_price, aut_name, cate_descrip, pub_name FROM category INNER JOIN purchase ON category.cate_id = purchase.cate_id INNER JOIN  book_mast ON purchase.book_name = book_mast.book_name INNER JOIN publisher ON book_mast.pub_id = publisher.pub_id INNER JOIN author ON publisher.country = author.country;", function(err, rows) {
        if (err) {
            console.log("PARA", err);
        } else {
            result += tabledrawer(rows);
        }
        res.send(result);
    });
});

app.listen(3000, function(){
    console.log("server running");
})