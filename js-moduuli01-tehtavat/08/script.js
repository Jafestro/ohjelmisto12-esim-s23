'use strict';

const parentListElement = document.querySelector('#list');

function isLeapYear(yearInput) {
    return yearInput % 4 === 0 && yearInput % 100 !== 0 || yearInput % 400 === 0;
}

const startYear = parseInt(prompt('Give start year'));
const endYear = parseInt(prompt('Give end year'));
let yearNow = startYear;


while (yearNow !== endYear) {
    if (isLeapYear(yearNow)) {
        const listElem = document.createElement("li");
        listElem.innerHTML = `${yearNow}`;
         parentListElement.append(listElem);
    }
    if (startYear > 0 && endYear < 0)
        yearNow--;
    else
        yearNow++;
}