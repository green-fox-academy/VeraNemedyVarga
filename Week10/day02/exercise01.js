'use strict'

// Create a constructor for creating Animals.
// it should take one parameter: what the animal says
// Every animal should have a method called say() that prints what the animal says

class Animal {
    constructor (itSays) {
        this.itSays = itSays;
    }

    say() {
        console.log(this.itSays);
    }
}

let rabbit = new Animal("Fuff");
rabbit.say();

Animal.prototype.hairiness = "very";
console.log(rabbit.hairiness);
