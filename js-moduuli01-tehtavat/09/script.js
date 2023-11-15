'use strict';

function isPrime(luku) {
    luku = parseInt(luku)
    if (luku <= 1)
        return false;
    else {
        for (let i = 2; i <= (luku ** 0.5); i++) {
            if (luku % i === 0 && luku !== i)
                return false;
        }
        return true;
    }
}


const num = parseInt(prompt('Give me a number so I can tell you if it is a prime number or not'));
const primeElem = document.querySelector('#prime');
if (isPrime(num))
    primeElem.innerHTML = `${num} is prime number`
else
    primeElem.innerHTML = `${num} is NOT a prime number`
