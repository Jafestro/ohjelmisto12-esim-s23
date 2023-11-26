'use strict';

const operationElem = document.querySelector('#operation');
const num1Elem = document.querySelector('#num1');
const num2Elem = document.querySelector('#num2');
const buttonElem = document.querySelector('#start');
const resultELem = document.querySelector('#result');

function doMath() {
    const number1 = parseFloat(num1Elem.value);
    const number2 = parseFloat(num2Elem.value);
    const operation = operationElem.value;
    let result = 0;
    switch (operation) {
        case 'add':
            result = number1 + number2;
            resultELem.innerHTML = result;        
            break;
        case 'sub':
            result = number1 - number2;
            resultELem.innerHTML = result;        
            break;
        case 'multi':
            result = number1 * number2;
            resultELem.innerHTML = result; 
            break;
        case 'div':
            result = number1 / number2;
            resultELem.innerHTML = result; 
            break;
        }
}

buttonElem.addEventListener('click', doMath);

