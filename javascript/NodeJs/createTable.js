import { createConnection } from 'mysql';

var con = createConnection({
    host: 'localhost',
    user:'root',
    password : 'Bakari@1',
    database : 'myTest'
});

con.connect(function(err){
    if(err) throw err;
    console.log("Database connected successfuly");
    var sql = "CREATE TABLE customer (id INT(10),username VARCHAR(25),password VARCHAR(25))";
    con.query(sql,function(err,result){
        if (err) throw err;
        console.log("table create!"+result);
    });
});