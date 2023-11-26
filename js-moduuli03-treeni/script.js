'use strict';
console.clear();
// BOM browser object model
console.log(window);
// window.alert('Moro');
// alert('Moro');

// confirm returns boolean value (true/false)
// if(confirm('Ookko tosissas?')) {
//     console.log('Kayttaja klikkasi ok');
// }
// else {
//     console.log('kayttaja painoi "Peruuta"');
// }
// //prompt palauttaa kayttajan syottaman merkkijonon, jos painetaan ok
// // palauttaa null, jos painetetaan cancel
// console.log(prompt('Sano jotain!'));

// DOM Document object model
console.log(window.document);

// const targetElements = document.getElementsByTagName('p');
// console.log(targetElements);

// tagname
const targetElements = document.querySelectorAll('p');
console.log(targetElements);

//id
const targetElement = document.querySelector('#toka');
console.log(targetElement);

targetElement.textContent = 'Meow';


//HTML-elementtien luominen ja lisaaminen DOMiin
const newP = document.createElement('p');

document.querySelector('article').append(newP);
// newP.innerText = '<b> Meowwwwwiwww </b>';
newP.innerHTML = "Tassa jotain <b> uutta </b> juttua.";
newP.classList.add('blue');
newP.classList.add('bold');


// viittaus kaikkiin p-elementteihin loytyy targetElements-muuttujan
//kasitellaan ensimmaista niista
targetElements[0].classList.add('bold', 'red');
// targetElements[0].classList.remove('red');

// tapahtumankasittely
function clickHandler(event) {
    console.log('p clicked', event);
    targetElements[0].classList.remove('red');
}

targetElements[0].addEventListener('click', clickHandler);


//kakkosklikin (context menu) kasittely(nimeton funktiota)
targetElements[0].addEventListener('contextmenu', function(event){
    console.log('context menu');
    event.preventDefault();
});

// key loggeri
const keyPressHistory = [];
document.addEventListener('keyup', function(event) {
    console.log('nappain ylos', event.key);
    keyPressHistory.push(event.key);
    console.log('nappainpainallushistoria', keyPressHistory.toString());
});

// hiirenseuranta

document.addEventListener('mousemove', function(event){
    console.log('mouse position', event.clientX, event.clientY);
});