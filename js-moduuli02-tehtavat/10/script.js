'use strict';

function compare(b, a){
    if(a.votes > b.votes)
        return 1;
    else if(a.votes < b.votes)
        return -1;
    else
        return 0; 
}


const count = parseInt(prompt('Enter the number of the candidates'));
const candidates = [];

for (let index = 0; index < count; index++) {
    let nimi = prompt(`Name for candidate ${index + 1}`);
    candidates.push({name: nimi, votes: 0});
}

const votersCount = parseInt(prompt('Enter voters count'));

for (let index = 0; index < votersCount; index++) {
    const candidateName = prompt('To whom you are giving your vote to?');
    const index = candidates.findIndex(candidate => candidate.name === candidateName);
    if(index !== -1){
        candidates[index].votes++;
    }
}

candidates.sort(compare);
console.log(`The winner is ${candidates[0].name} with ${candidates[0].votes} votes.`);
console.log('results:');
candidates.forEach(candidate => console.log(`${candidate.name}: ${candidate.votes} votes`));