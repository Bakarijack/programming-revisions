let o = {};
o.x = 1;

let p = Object.create(o);
p.y = 2;

let q = Object.create(p);
q.z = 4;

let f = q.toString();

q.x = 2;

console.log(f);
console.log(q.x + q.y);
console.log(q);

let unitcircle = {r:1};

let c = Object.create(unitcircle);
c.x = 1; c.y = 1;
c.r = 2;  //override the inherited property

console.log(c.r);
console.log(unitcircle.r);