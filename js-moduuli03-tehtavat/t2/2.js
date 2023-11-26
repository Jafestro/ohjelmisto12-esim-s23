'use strict';

const arr = ['First item', 'Second item', 'Third item'];
const targetElement = document.querySelector('#target');
for (let index = 0; index < arr.length; index++) {
    const list = document.createElement('li');
    list.innerHTML = arr[index];
    if(index === 1)
        list.classList.add('my-item');
    targetElement.appendChild(list);
}
