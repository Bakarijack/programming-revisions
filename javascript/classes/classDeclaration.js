//method 1 for declaring the class (class declaration method)
class Geometry{
    constructor(color){
        this.color = color;
    }

    
}
class Rectangle extends Geometry{
    constructor(height,width,color){
        super(color);
        this.height = height;
        this.width = width;
    }
}


//method2 for declaring a class is (class expression)
//1.Unamed expression
let Circle = class{                     
    constructor(radius){
        this.radius = radius;
    }
}

//2. named expression
let Triangle2 = class Triangle{
    constructor(height,base){
        this.height = height;
        this.base = base;
    }
}

console.log(Triangle2.name); //chaecking the name of the original class Triangle

console.log(Circle.name);         //Circle

const rect1 = new Rectangle(1,3,"red");
console.log(rect1.color);