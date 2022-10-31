let data = [1,2,3,4,5,6,7,8,9],sum = 0;

for(let element of data){
    sum += element;
}

console.log(sum);

//with objects use Object.keys()
let o = {x:1,y:2,z:3};
let keys = "";
for(let k of Object.keys(o)){
    keys += k;
}
console.log(keys);

let sum2 = 0;
for(let v of Object.values(o)){
    sum2 += v;
}
console.log(sum2);

//using Object.entries() with distructuring assignment
let pairs = "";
for(let [k,v] of Object.entries(o)){
    pairs += k + v;
}
console.log(pairs);

//with strings
let frequency = {};
for(let letter of "Bakari"){
    if(frequency[letter]){
        frequency[letter]++;
    }else{
        frequency[letter] = 1;
    }
}
console.log(frequency);

//with set and maps
let text = "Na na na na Bakari";
let wordSet = new Set(text.split(" "));
let unique = [];
for(let word of wordSet){
    unique.push(word);
}
console.log(unique);

//with the maps
let m = new Map([[1,"one"]]);
for(let [k,value] of m){
    console.log(k);
    console.log(value);
}

//with asynchronous iterator
async function printStream(stream){
    for await (let chunk of stream){
        console.log(chunk);
    }
}

printStream("Bakari");
