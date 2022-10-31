var canvas = undefined;
var canvasContext = undefined;
const myTimeout = setTimeout(hello,5000);

function hello(){
    document.getElementById('title').innerHTML="Game dashbord";
}

function clearDashbord(){
    clearTimeout(myTimeout);   //only stops the setTimeout from continueing running
}

function start(){
    canvas = document.getElementById("canvasArea");
    canvasContext = canvas.getContext('2d');
    window.setTimeout(mainLoop,5000);
    mainLoop();
}

document.addEventListener("DOMContentLoaded",start);

function update(){}

function draw(){}

function mainLoop(){
    canvasContext.fillStyle = "blue";
    canvasContext.fillRect(0,0,canvas.width,canvas.height);
    update();
    draw();
    window.setTimeout(mainLoop,1000 / 60);
}