'use strict';

const firstElem = document.querySelector('input[name="firstname"]');
const lastElem = document.querySelector('input[name="lastname"');
const submit = document.querySelector('input[type="submit"]');

function sayMyName(){
    const p = document.querySelector('#target');
    p.innerHTML = `Your name is ${firstElem.value} ${lastElem.value}`    
}

submit.addEventListener('click', function(event){
    sayMyName();
    event.preventDefault();
});