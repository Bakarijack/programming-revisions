var mysql = require('mysql');

var con = mysql.createConnection({
    host:'localhost',
    user: 'root',
    password: 'Bakari@1'
});

con.connect(function(err){
    if(err) throw err;
    console.log('Connected to database successfuly');
    con.query("CREATE DATABASE myTest", function(err,result){
        if(err) throw err;
        console.log("Database created successfuly");
    });
});