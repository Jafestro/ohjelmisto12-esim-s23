'use strict';

const numberOfParticipants = parseInt(prompt('Give the number of the participants'));
const arr = [];

const parentOrderedList = document.querySelector('#Participants');

for (let i = 0; i < numberOfParticipants; i++) {
    const name = prompt(`Name of the participant ${i + 1}`);
    arr.push(name);
}
arr.sort()
for (let i = 0; i < numberOfParticipants; i++) {
    const childList = document.createElement('li');
    childList.innerHTML = `${arr[i]}`;
    parentOrderedList.append(childList);
}