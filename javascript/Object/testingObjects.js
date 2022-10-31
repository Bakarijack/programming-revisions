//using in operator
let o = {x:1};
console.log("x" in o);
console.log("y" in o);
console.log("toString" in o);

//using hasOwnProperty()
console.log(o.hasOwnProperty("x"));
console.log(o.hasOwnProperty("y"));
console.log(o.hasOwnProperty("toString"));