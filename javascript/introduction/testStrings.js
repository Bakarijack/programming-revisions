var firstName = "Bakari";

var firstChar = firstName.charAt(0);
//console.log(firstChar);
var count = 0;
for (var i = 0 ; i < firstName.length ; i++){
    if (firstName.charAt(i) === "a"){
        count++;
    }
}

//console.log(count);
var names = "Bakari Mtua Kilu Rehema Kamene Kilu Ibrahim Shokowa Kilu Saumu Kanini Kilu Ibrahim Shokowa";
var searchedName = "Ibrahim Shokowa";
var replaceName = "Jamal Mangi";

var newNames = names.replace(/Ibrahim Shokowa/g,replaceName);

console.log(newNames);