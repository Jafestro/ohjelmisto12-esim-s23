'use strict';

function even(arr){
    const evens = [];
    for (let index = 0; index < arr.length; index++) {
        const element = arr[index];
        if (element % 2 === 0)
            evens.push(element);
    }
    return evens;
}


const arr = [2,7,4];
const evens = even(arr);

console.log(arr);
console.log(evens);
