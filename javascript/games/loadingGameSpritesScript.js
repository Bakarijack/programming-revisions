"use strict";
var Game = {
    canvas : undefined,
    canvasContext : undefined,
    assetImage: undefined,
    assetImagePosition: {x: 0, y: 50},
    backgroundSprite : undefined,
    backgroundMusic : undefined
};

Game.start = function() {
    Game.canvas = document.getElementById('gameArea');
    Game.canvasContext = Game.canvas.getContext('2d');
    Game.assetImage = new Image();
    Game.backgroundSprite = new Image();
    Game.backgroundSprite.src = "unreal.jpg";
    Game.assetImage.src = "png/Idle (1).png";
    Game.backgroundMusic = new Audio();
    Game.backgroundMusic.src = "Hukumu na adabu za swawm 03 – al-Firqah an-Naajiyah.mp3";
    Game.backgroundMusic.volume = 1;
    Game.backgroundMusic.play();
    window.setTimeout(Game.mainLoop, 500);
};

document.addEventListener("DOMContentLoaded",Game.start);

Game.drawImage = function (sprite,position){
    Game.canvasContext.save();
    Game.canvasContext.translate(position.x,position.y);
    Game.canvasContext.drawImage(sprite,0,0,sprite.width,sprite.height,0,0,sprite.width,sprite.height);
    Game.canvasContext.restore();
};

Game.update = function () {
    var d = new Date();
    Game.assetImagePosition.x = d.getTime() % Game.canvas.width;
};

Game.draw = function () {
    Game.drawImage(Game.backgroundSprite, {x:0, y: 0});
    Game.drawImage(Game.assetImage, Game.assetImagePosition);

};

Game.clearCanvas = function () {
    Game.canvasContext.clearRect(0,0,Game.canvas.width,Game.canvas.height);
};

Game.mainLoop = function (){
    Game.clearCanvas();
    Game.update();
    Game.draw();
    window.setTimeout(Game.mainLoop, 1000/60);
};