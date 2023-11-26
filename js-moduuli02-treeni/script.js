'use strict';

function arrayTest(numbers){
    numbers.push(9);
    return numbers;
}

const numbers = [1,2,3];



const numbers2 = numbers; //kopioidaan viittaus uuteen muuttujaan
let numbers3 = []; // uuteen taulukon luominen ja olemassa 
numbers3 = numbers3.concat(numbers);

//Toinrn tapa kopioida arvot uuteen taulukkoon
const numbers4 = [numbers];

//toinen tapa tekeminen concat
const numbers5 = [...numbers]; // ...[1,2,3] => 1, 2, 3 
console.clear();
console.log('numbers5', ...numbers)



console.log('funktion paluu arvo', arrayTest(numbers));
console.log('alkuperäinen taulukko', numbers);
console.log('kopioutu taulukko ', numbers2);
console.log('"kopiodut" taulukon arvot', numbers3);


console.log('numbers 4', numbers4);
