'use strict';

const isConfirmed = confirm('Should I calculate the square root?');
const numberElem = document.querySelector('#number');
if (isConfirmed) {
    const number = parseInt(prompt('Give a number'));
    if (number >= 0) {
        const sqrtNumber = Math.sqrt(number);
        numberElem.innerHTML = `Square root of ${number} is ${sqrtNumber}`;
    } else {
        numberElem.innerHTML = 'The square root of a negative number is not defined';
    }
} else {
    numberElem.innerHTML = 'The square root is not calculated.';
}