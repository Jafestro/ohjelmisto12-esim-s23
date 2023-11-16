'use strict';

function concat(strings){
    let concated = '';
    for (let index = 0; index < strings.length; index++) {
        concated += strings[index];
    }
    return concated;
}


const arr = ['Johnny', 'Deedee', 'Joey', 'Marky'];

const concatElem = document.querySelector('#concat');
concatElem.innerHTML = concat(arr);