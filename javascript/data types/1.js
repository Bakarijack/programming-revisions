//BigInt
const value1 = 900719925124740998n;

//adding two  big integers
const result1 = value1 + 1n;
console.log(result1);

const value2 = 900719925124740998n;
//error! big int and number cannot be added 
const result2 = value2 + 1;
console.log(result2);