'use strict';

const diceRolls = parseInt(prompt('Number of rolls'));
let summa = 0;
for (let i = 0; i < diceRolls; i++) {
    const diceRoll = Math.floor(Math.random() * 5) + 1; //Se antaa numeroita 1-6 välillä
    summa += diceRoll;
}
const diceElement = document.querySelector('#dice');
diceElement.innerHTML = `Sum of dice rolls is ${summa}`;


//ToDo add comments to every assignment not only to this one