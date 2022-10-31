//first method
var name = [];
name.push('bakari');
console.log(name);
name.push('kilu');
console.log(name);

//second method using new operator
var arr = new Array(2);                     //create the length of the array
var arr1 = new Array(2,4,6,3);             //create the array with the given elements
arr.push(1);
console.log(arr);
console.log(arr1);

//third method using the Array.from()
var worker = Array.from({length : 2});
console.log(worker)
worker[0] = "Mtua"; worker[1] = 'Kilu';
console.log(worker);
console.log(worker[3]);

//copy the array
var worker1 = Array.from(name);
console.log(worker1);

//using Array.of()
var age = Array.of(27);
console.log(age);
var age2 = Array(5);
console.log(age2);   //equal to new Array(5)