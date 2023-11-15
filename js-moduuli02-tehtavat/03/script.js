'use strict';

const parentList = document.querySelector('#dogs');
const arr = [];
for (let i = 0; i < 6; i++) {
    const dogName = prompt(`Give ${i+1}. dog's name`);
    arr.push(dogName);
}

arr.reverse();

let mystr = '';

for (let i = 0; i < arr.length; i++) {
    mystr += `<li>${arr[i]}</li>`
}
parentList.innerHTML = mystr;