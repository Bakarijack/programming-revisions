let book = {
    for: "audients",
    author:{
        name:"bakari",
        email:"bakarikilu254@gmail.com"
    }
};

console.log(book.author.email);

//creating using new keyword
let d = new Date();
console.log(d.getDate())

let literatureBooks = Object.create(book);
console.log(literatureBooks.for);

export {book};