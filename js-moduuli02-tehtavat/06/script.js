'use strict';

function heittoNoppa(){
    return Math.floor(Math.random() * 6 + 1);
}


let result = 0;
let myStr = "";

while(result !== 6){
    result = heittoNoppa();
    myStr += `<li> ${result} </li>`;
}

const parentList = document.querySelector('#ul');
parentList.innerHTML = myStr;