'use strict';

const yearInput = parseInt(prompt('Enter a year to check if it is a leap year or not😀'));
const element = document.querySelector(".year");
if (yearInput % 4 === 0 && yearInput % 100 !== 0 || yearInput % 400 === 0) {
    element.innerHTML = `${yearInput} is a leap year!`;
} else {
    element.innerHTML = `${yearInput} is not a leap year!`;
}