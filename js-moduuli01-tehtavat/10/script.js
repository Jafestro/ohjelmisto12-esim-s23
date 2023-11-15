'use strict';

function calcSumProbability(diceCount, sum) {
        let counter = 0;
        for (let i = 0; i < 10000; i++) {
                let summa = 0;
                for (let j = 0; j < parseInt(diceCount); j++) {
                        summa += (Math.floor(Math.random() * 6) + 1); //se antaa numeroita 1-6 valilla
                }
                if (summa === parseInt(sum))
                        counter++;
        }
        return ((counter/10000) * 100).toFixed(2);
}

const diceElem = document.querySelector('#dice');
const inputDice = parseInt(prompt('Give dice count'));
const inputSum = parseInt(prompt('Give the sum probability that you what to calculate.'));

const probability = calcSumProbability(inputDice,inputSum);
diceElem.innerHTML = `Probability to get sum ${inputSum} with ${inputDice} dice is ${probability}%`