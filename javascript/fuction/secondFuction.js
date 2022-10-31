//Use of the return
function a(){
    var result;
    result = concatenate('Bakari','Jack');
    document.write(`Hello ${result}!`);
}
function concatenate(first,second){
    var full;
    full = first+second;
    return full;
}
