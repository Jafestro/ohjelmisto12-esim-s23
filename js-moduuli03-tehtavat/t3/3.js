'use strict';
const names = ['John', 'Paul', 'Jones'];
const targetElement = document.querySelector('#target');
for (let index = 0; index < names.length; index++) {
    const list = document.createElement('li');
    list.innerHTML = names[index];
    targetElement.appendChild(list);
}