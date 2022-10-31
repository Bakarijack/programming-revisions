import {change} from './testCnst.js';

//using an assingment operator
const numbers = [];

numbers.push(1);   //inserting elements at the end of the array
numbers.push(5);
numbers.push(3,7);  //insert multiple elements

console.log(numbers);

numbers.unshift(0);  //insert element at the begining of the array

console.log(numbers);

//using the new operator 
const letters = new Array(3);

letters.push('a');
letters.unshift('b');

console.log(letters);

//using array.from()

const ltrs = Array.from(letters);      //copy one array the the other

console.log(ltrs);

const num1 = Array.from({length: 3});  //create an array of length 3

num1.push(12);
num1.unshift(45);
num1[2] = 23;
num1[1] = 16;

console.log(num1);

//using spread operator
const num2 = [...num1];   //uses ... to copy the content of one array the other array

console.log(num2);

//using Array()
const names = Array("Bakari","Mtua");   //passing single number create the array whose length is equal to that number

console.log(names);

//using Array.of()
const evenNums = Array.of(2);

console.log(evenNums);

let prod = change(3,4);

console.log(prod);