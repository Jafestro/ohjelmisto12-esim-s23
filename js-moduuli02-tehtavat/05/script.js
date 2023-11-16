'use strict';

const arr = [];

while (true){
    const input = parseInt(prompt('Enter a number'));
    if (arr.includes(input))
        break;
    arr.push(input);
}

arr.sort(function(a,b){return a - b;})

for (let index = 0; index < arr.length; index++) {
    const element = arr[index];
    console.log(element);
}