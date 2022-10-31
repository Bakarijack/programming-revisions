var names = "Bakari Mtua Kilu Rehema Kamene Kilu Ibrahim Shokowa Kilu Saumu Kanini Kilu";
var searchedName = "Ibrahim Shokowa";
var searchedNameIndex = names.indexOf(searchedName);

var reName = " Jamal Mangi ";
if(searchedName !== -1){
    names = names.slice(0,searchedNameIndex)+reName+names.slice(searchedNameIndex+searchedName.length);
}

//alert(names);
console.log(names);
var lastName = `family names are : "${names}"`;
console.log(lastName);