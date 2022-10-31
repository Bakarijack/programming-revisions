function sum(num1,num2){
    return num1 / num2;
}

try{
    var answer = sum(2,0);
    console.log(answer);
}catch(e){
    console.log("error: null function");
}