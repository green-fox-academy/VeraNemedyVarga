'use strict';
// - Create a function called `printer`
//   which logs to the console the input parameters
//   (can have multiple number of arguments)

function printer() {
    arguments;
    for (var element = 0; element < arguments.length; element++) {
        console.log(arguments[element]);
    }
}

printer("whatever", "still whatever");
