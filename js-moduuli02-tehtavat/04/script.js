'use strict';

let input = 1;
const arr = [];

while (input !== 0) {
   input = parseInt(prompt('Give a number (enter 0 to exit)'));
   if (input !== 0)
    arr.push(input);
}

arr.sort(function(a,b){return b - a}); // Anna meille reverse function mutta toimivaaaa

for (let index = 0; index < arr.length; index++) {
    const element = arr[index];
    console.log(element);
}