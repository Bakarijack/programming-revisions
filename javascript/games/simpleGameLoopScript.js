"use strict";

var Game = {
    canvas : undefined,
    canvasContext: undefined,
    rectanglePositionx : 0,
    rectanglePositiony : 0,
    balloonSprite: undefined
};

Game.start = function (){
    Game.canvas = document.getElementById('gameArea');
    Game.canvasContext = Game.canvas.getContext('2d');
    Game.mainLoop();
};

document.addEventListener("DOMContentLoaded",Game.start);

Game.update = function (){
    var d = new Date();
    Game.rectanglePositionx = d.getTime() % Game.canvas.width; 
    Game.rectanglePositiony = d.getTime() % Game.canvas.width; 

};

Game.draw = function (){
    Game.canvasContext.fillStyle = "blue";
    Game.canvasContext.fillRect(Game.rectanglePositionx,Game.rectanglePositiony,50,50);
};

Game.clearCanvas = function (){
    Game.canvasContext.clearRect(0,0,Game.canvas.width,Game.canvas.height);
};

Game.mainLoop =  function (){
    Game.clearCanvas();
    Game.update();
    Game.draw();
    window.setTimeout(Game.mainLoop, 1000/60);
};