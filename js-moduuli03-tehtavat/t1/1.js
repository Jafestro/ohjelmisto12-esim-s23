'use strict';

const targetElement = document.querySelector('#target');
const myStr = '<li>First item</li>\n<li>Second item</li>\n<li>Third item</li>';
targetElement.innerHTML = myStr;
targetElement.classList.add('my-list');