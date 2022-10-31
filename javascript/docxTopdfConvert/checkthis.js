let User = function (){

};

//User.prototype.start = function(){}

class Student {
    constructor() {
        this.name = "bakari";
        this.gender = "male";
    }
}

Student.prototype.age = 25;

let student1 = new Student();
console.log(student1.gender);
console.log(student1.age);

let student2 = new Student();
console.log(student2.age);

var str = (function(t){        //the function is executed immediately without being assigned to a variable
   // console.log("hello world"+t);
   return t;
})("bakari");   //the parenthesis at the end couse this execution

console.log(str);