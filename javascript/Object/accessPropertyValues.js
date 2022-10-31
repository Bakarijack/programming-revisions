import {book} from "./litearalObjects.js";
let o = {x: 1,y:{z:3}};
let a =[o,4,[1,6]];

console.log(o.x);
console.log(o.y.z);
console.log(a[0].x);
console.log(a[1]);
console.log(a[0]["x"]);
console.log(a[2][1]);
console.log(book.author.name);
console.log(book.author.email);
console.log(book.toString());
