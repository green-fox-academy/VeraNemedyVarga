'use strict';

// Create a constructor for creating Rectangles.
// it should take two parameters: the sides of the rectangle
// Every rectangle should have a method called getArea() that returns its area
// Every rectangle should have a method called getCircumference() that returns its circumference

function Rectangles(A, B) {
    this.sideA = A;
    this.sideB = B;
}

Rectangles.prototype.getArea = function () {
    console.log(this.sideA * this.sideB);
}

Rectangles.prototype.getCircumference = function() {
    console.log(2 * (this.sideA + this.sideB));
}

let rectangle = new Rectangles(4, 3);
rectangle.getArea();
rectangle.getCircumference();


//factory pattern

function Rectangle(C, D) {
    var oneSide = C;
    var otherSide = D;

    function getFactoryArea(){
        console.log(C * D);
    }

    function getFactoryCircumference () {
        console.log(2*(C + D));
    }

    return {
        getFactoryCircumference: getFactoryCircumference,
        getFactoryArea: getFactoryArea
    }
}

let rect = Rectangle(5, 3);
rect.getFactoryArea();
rect.getFactoryCircumference();
