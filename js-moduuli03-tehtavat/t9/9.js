'use strict';

const inputElem = document.querySelector('#calculation');
const resultElem = document.querySelector('#result');
const buttonElem = document.querySelector('#start');


function doMath(){
    const input = inputElem.value;
    if(input.includes('+')){
        const arr = input.split('+');
        resultElem.innerHTML = `${parseInt(arr[0]) + parseInt(arr[1])}`;
    }
    else if(input.includes('-')){
        const arr = input.split('-');
        resultElem.innerHTML = `${parseInt(arr[0]) - parseInt(arr[1])}`;
    }
    else if(input.includes('*')){
        const arr = input.split('*');
        resultElem.innerHTML = `${parseInt(arr[0]) * parseInt(arr[1])}`;
    }
    else if(input.includes('/')){
        const arr = input.split('/');
        resultElem.innerHTML = `${parseInt(arr[0]) / parseInt(arr[1])}`;
    }
}

buttonElem.addEventListener('click', doMath);