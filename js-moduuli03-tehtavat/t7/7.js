'use strict';

const p = document.querySelector('#trigger');
const img = document.querySelector('#target');

p.addEventListener('mouseover', function(){
    img.src = "img/picB.jpg";
});

p.addEventListener('mouseout', function(){
    img.src = "img/picA.jpg";
});