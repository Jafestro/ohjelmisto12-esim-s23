'use strict';

function heittoNoppa(max){
    return Math.floor(Math.random() * max + 1);  // se antaa meille silmalukuja 1-max välillä
}


let result = 0;
const max = parseInt(prompt('Enter max count of dice'));
let myStr = "";

while(result !== max){
    result = heittoNoppa(max);
    myStr += `<li> ${result} </li>`;
}

const parentList = document.querySelector('#ul');
parentList.innerHTML = myStr;