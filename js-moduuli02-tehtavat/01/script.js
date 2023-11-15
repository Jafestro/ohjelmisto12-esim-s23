'use strict';

let arr = [];
for (let i = 0; i < 5; i++) {
    const input = parseInt(prompt('Give number'));
    arr.push(input);
}

for (let i = arr.length - 1; i >= 0; i--) {
    console.log(arr[i]);
}