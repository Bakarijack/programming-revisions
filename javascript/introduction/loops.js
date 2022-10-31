var cityToCheck = prompt("Enter the city you live in. ");
//alert(cityToCheck.toLowerCase());
var cities = ["mombasa","malindi","lamu","nairobi","kisumu"];
var flag = false;

for(var i = 0 ; i < cities.length; i++){
    if(cities[i] === cityToCheck.toLowerCase()){
        alert(cityToCheck+" is among the big five cities in Kenya");
        flag = true;
        break;
    }
}

if(flag === false){
    alert(cityToCheck+" is not among the big five cities in Kenya");
}