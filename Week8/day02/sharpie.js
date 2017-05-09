// Create a Sharpie Constructor:
// We should know about each sharpie their color (which should be a string), width (which will be a floating point number), inkAmount (another floating point number)
// When creating one, we need to specify the color and the width
// Every sharpie is created with a default 100 as inkAmount
// We can use() the sharpie objects
// // which decreases inkAmount by the width

function sharpie(color, width, inkAmount = 100){
    this.color = color;
    this.width = width;
    this.inkAmount = inkAmount;
    this.use = function() {
        this.inkAmount -= this.inkAmount * this.width;
        return this.inkAmount;
    }
};

var pen = new sharpie("blue", 0.4, 40)
console.log(pen);
var usedPen = pen.use();
console.log(usedPen);
